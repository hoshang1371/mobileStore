from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token

from mobileStore_order.models import Order

from .serializer import PostAddressDetailSerializer,\
                        PostAddressDetailSerializer_for_Peyment,\
                        PaymentMethodeDetailSerializer,\
                        PostAddressSerializer,\
                        PaymentMethodeDetail
                        # PostPriceSerializer 

from .models import (
                    # PostPrice,
                    PostAddressDetail,
                    PostAddress
                    )

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView, 
    # RetrieveAPIView, 
    # RetrieveUpdateDestroyAPIView,
    # DestroyAPIView,
    # UpdateAPIView
    )

class PostAddressDetail_selected(ListCreateAPIView):
    queryset = PostAddressDetail.objects.all()
    serializer_class = PostAddressDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request,id, *args, **kwargs):
        user = Token.objects.get(pk=request.auth).user
        order = Order.objects.filter(owner=user,id=id)
        print(order)
        postAddressDetail = PostAddressDetail.objects.filter(OrderDetailSelected=order[0]).first()
        print(postAddressDetail.PostPriceSelected.title)
        print(postAddressDetail.PostPriceSelected.price)

        return JsonResponse({
                    "title": postAddressDetail.PostPriceSelected.title,
                    "price": postAddressDetail.PostPriceSelected.price,
                    }, safe=False)
    
class PostAddressDetail_peyment(ListAPIView):
    queryset = PostAddressDetail.objects.all()
    serializer_class = PostAddressDetailSerializer_for_Peyment
    permission_classes = (IsAuthenticated,)

class PaymentMethodeDetail_peyment(ListAPIView):
    queryset = PaymentMethodeDetail.objects.all()
    serializer_class = PaymentMethodeDetailSerializer
    permission_classes = (IsAuthenticated,)


class PostAddress_get(ListAPIView):
    queryset = PostAddress.objects.all()
    serializer_class = PostAddressSerializer
    permission_classes = (IsAuthenticated,)

class peymentAndSendMethode(ListCreateAPIView):
    queryset = PaymentMethodeDetail.objects.all()
    serializer_class = PaymentMethodeDetailSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = Token.objects.get(pk=request.auth).user
        # print(user)
        print(request.data)
        req = request.data
        Order_id = request.data['Order_id']
        order = Order.objects.filter(owner=user,id=Order_id)
        # print(request.data['send'])
        # print(request.data['peyment'])
        # print(request.data['rull'])
        postAddressDetail = PostAddressDetail.objects.filter(OrderDetailSelected=order[0]).first()
        postAddressDetail.carrierDetails = request.data['send']
        postAddressDetail.save()
        # print(postAddressDetail.carrierDetails)
        #! age sakhte nashodebod
        # paymentMethodeDetail = PaymentMethodeDetail.objects.get(OrderDetailSelected=order[0])
        paymentMethodeDetail, created = PaymentMethodeDetail.objects.get_or_create(OrderDetailSelected=order[0])
        paymentMethodeDetail.PaymentDetails=request.data['peyment']
        paymentMethodeDetail.isTermsAndRules = request.data['rull']
        paymentMethodeDetail.save()

        if(paymentMethodeDetail.PaymentDetails == "ثبت سفارش (پیش فاکتور)"):
            return JsonResponse({
                    "code": "1",
                    }, safe=False)
        elif(paymentMethodeDetail.PaymentDetails == "پرداخت از طریق درگاه پرداخت اینترنتی"):
                return JsonResponse({
                    "code": "2",
                    }, safe=False)
        # print(paymentMethodeDetail.PaymentDetails) 
        # print(paymentMethodeDetail.isTermsAndRules)




        return JsonResponse({
                    "title": "postAddressDetail.PostPriceSelected.title",
                    "price": "postAddressDetail.PostPriceSelected.price",
                    }, safe=False)