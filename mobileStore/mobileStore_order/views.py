from django.shortcuts import render

from mobileStore_product.models import Product

from .models import Order,OrderDetail

from .serializer import OrderProductSerializer,DeleteOrderDetailSerializer

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
    # UpdateAPIView
    )

class product_order(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderProductSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = Token.objects.get(pk=request.auth).user
        order = Order.objects.filter(owner=user,is_paid=False).first()
        orderDetails =order.orderdetail_set.all()
        serializer = OrderProductSerializer(orderDetails, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = Token.objects.get(pk=request.auth).user
        order = Order.objects.filter(owner=user,is_paid=False)
        if not order.exists():
            order =  Order.objects.create(owner=user)


        code = int(request.data.get('code'))
        count = int(request.data.get('count'))
        if count < 0:
            count = 1

        product = Product.objects.filter(code=code).first()


        if count > int(product.number):
            print("in tedad dar anbar mojod nist")
            return JsonResponse({
                    "massege": "no this count exist",
                    })
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
