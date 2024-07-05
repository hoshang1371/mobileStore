from django.shortcuts import render

from post_information.models import PostPrice
from mobileStore_product.models import Product

from .models import Order,OrderDetail

from .serializer import OrderProductSerializer,DeleteOrderDetailSerializer, OrderProductSerializerForListOfbuy

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http.response import HttpResponse, JsonResponse

from rest_framework.generics import (
    # ListAPIView,
    ListCreateAPIView, 
    # RetrieveAPIView, 
    # RetrieveUpdateDestroyAPIView,
    DestroyAPIView,
    UpdateAPIView
    )

class product_order(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderProductSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = Token.objects.get(pk=request.auth).user
        order = Order.objects.filter(owner=user,is_paid=False).first()


        # orderDetails =order.first().orderdetail_set.all()
        # serializer = OrderProductSerializer(orderDetails, many=True)
        # return Response(serializer.data)


        orderDetails =order.orderdetail_set.all()
        serializer = OrderProductSerializer(orderDetails, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = Token.objects.get(pk=request.auth).user
        order = Order.objects.filter(owner=user,is_paid=False)
        
        if not order.exists():
            order =  Order.objects.create(owner=user)

        print("===========================================")
        print(order)

        code = int(request.data.get('code'))
        count = int(request.data.get('count'))
        if count < 0:
            count = 1

        product = Product.objects.filter(code=code).first()

        #ToDO: fix IT 
        if count > int(product.number):
            # data = {
            #     'err':'not exist',
            #     'number': x[0].product.number
            # }
            print("in tedad dar anbar mojod nist")
            return JsonResponse({
                    "err": "no this count exist",
                    }, status=201)
        else:
            print("mojod dar anbar ast")
        # print("tedad",product.number)
        print(f"product_id={product.id}")
        print(order.first())

        x = order.first().orderdetail_set.filter(product_id=product.id)
        print(x)
        # print(type(product.priceOff))
        # print(type(count))

        if x:
            print("exist")
            print(x.values()[0]['count'])
            # x.update(count=count+x.values()[0]['count'])
            x.update(count=count)
            if product.priceOff is None:
                x.update(price=(product.price*count))
            else:
                x.update(price=(product.priceOff*count))
        else:
            # ! priceOff lahaz shavad
            print("NO exist")

            if product.priceOff is None:

                order.first().orderdetail_set.create(
                    product_id=product.id, price=(product.price*count), count=count)
            else:
                order.first().orderdetail_set.create(
                    product_id=product.id, price=(product.priceOff*count), count=count)
        # TODO: kol sabad kharid ra befrestad
        orderDetails =order.first().orderdetail_set.all()
        serializer = OrderProductSerializer(orderDetails, many=True)
        return Response(serializer.data)
        # return Response(request.data)


class DeleteOrderDetail(DestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = DeleteOrderDetailSerializer
    permission_classes = [IsAuthenticated]

class product_orders_details_List_buy(UpdateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderProductSerializerForListOfbuy
    permission_classes = [IsAuthenticated]
    def put(self, request, *args, **kwargs):
        user = Token.objects.get(pk=request.auth).user
        order = Order.objects.filter(owner=user,is_paid=False).first()

        orderDetails =order.orderdetail_set.all()
        serializer = OrderProductSerializer(orderDetails, many=True)

        orderDetailsRes = request.data.get('orderDetails')

        # errorData =[]
        for orderDe,orderDeRes in zip(orderDetails,orderDetailsRes):

            if int(orderDeRes['count']) < 1:
                orderDeRes['count'] = "1"
            #! teedad hame check shavad
            
            # if int(orderDeRes['count']) > int(orderDe.product.number):
            #     data = {
            #         'product': orderDe.product.title,
            #         'number': orderDe.product.number
            #     }
            #     errorData.append(data)
            # print(f"errorData={errorData}")

            # if len(errorData) == 0:
            #     print("kirKhar")


            if orderDe.product.priceOff is None:
                orderDe.price = (int(orderDeRes['count'])*orderDe.product.price)
            else:
                orderDe.price = (int(orderDeRes['count'])*orderDe.product.priceOff)
            orderDe.count = orderDeRes['count']
            orderDe.save()
        # print("========================================")

        # orderDetails.update(orderDetailsRes[0])
        # return JsonResponse({
        #             "err": "no this count exist", orderDetails
        #     })
        # return JsonResponse(data, safe=False, status=201)
        # if len(errorData) == 0:
        return Response(serializer.data)
        # else:
            # return JsonResponse(errorData, safe=False, status=201)

class product_order_List_buy(UpdateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderProductSerializerForListOfbuy
    permission_classes = [IsAuthenticated]
    # lookup_field = 'id'
    def put(self, request, *args, **kwargs):
        user = Token.objects.get(pk=request.auth).user
        order = Order.objects.filter(owner=user,is_paid=False).first()

        if order is None:
            order = Order.objects.create( owner=user, is_paid=False)
        orderdetail_product_code = int(request.data.get('id'))
        count = int(request.data.get('count'))

        post_price = PostPrice.objects.filter().first()
        if count < 1:
            count = 1
            
        x = order.orderdetail_set.filter(id=orderdetail_product_code)
        if count > int(x[0].product.number):
            data = {
                'err':'not exist',
                'number': x[0].product.number
            }
            return JsonResponse(data, safe=False, status=201)

        if x:
            #* gheymat ham bayad barrasi shavad
            if x[0].product.priceOff is None:
                x.update(price=(count*x[0].product.price))
            else:
                x.update(price=(count*x[0].product.priceOff))
            x.update(count=count)


        order_partials_buy = order.orderdetail_set.all()

        Total_price_for_all_product_buy =0
        count_of_all_product =0
        count_all=0
        #* barrasi shavad
        # Total_price_for_each_product_buy=0
        for order_partial in order_partials_buy:
            count_of_all_product =count_of_all_product+1
            #* in barrasi shavad
            count_all =count_all +order_partial.count
            
            Total_price_for_each_product_buy = order_partial.price
            Total_price_for_all_product_buy = Total_price_for_all_product_buy + Total_price_for_each_product_buy
        Total_price_postPrice = Total_price_for_all_product_buy + post_price.price
        # print('count_all=',count_all);
        # print('Total_price_postPrice=',Total_price_postPrice);


        response = {
            "id": x.values()[0]['id'],
            "count": x.values()[0]['count'],
            "price": x.values()[0]['price'],
            "Total_price_for_all_product_buy" : Total_price_for_all_product_buy,
            "count_of_all_product" : count_of_all_product,
            "Total_price_postPrice" : Total_price_postPrice,
            "count_all" : count_all,
        }

        return JsonResponse(response, safe=False)

