from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from djoser import utils
from django.contrib.auth.tokens import default_token_generator
from rest_framework.response import Response

from .models import User
# from django.contrib.auth.models import User

# Create your views here.
class finishActiveEmail(APIView):
    # def post(self, request, *args, **kwargs):
    def get(self, request, *args, **kwargs):
        uid = self.kwargs.get('uid')
        token = self.kwargs.get('token')
        user = User.objects.filter(id=utils.decode_uid(uid))[0]
        # print(user)
        # print("uid=",uid)
        # print("utils=",utils.decode_uid(uid))
        # print("token=",token)
        # print("default_token_generator=", default_token_generator.check_token(user, token))
        # print("==========================")

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()

            return JsonResponse({
                    "massege": ".حساب کاربری شما فعال شد",
                    })
        
        return JsonResponse({
                "massege": "مشکل در فعال سازی حساب کاربری شما وجود دارد",
                })
    # def get(self, request, format=None):
    #     products = Product.objects.all().filter(active=True)[0:8]
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)

class finishForgetPass(APIView):
    def post(self, request, *args, **kwargs):
        uid = self.kwargs.get('uid')
        token = self.kwargs.get('token')
        print("uid=",uid)
        print("token=",token)
        print(request.data)
        print(request.data.get('password'))
        print(request.data.get('re_password'))

        password= request.data.get('password')
        re_password= request.data.get('re_password')


        user = User.objects.filter(id=utils.decode_uid(uid))[0]
        print(user)

        print("default_token_generator=", default_token_generator.check_token(user, token))
        print("==========================")
        if user is not None and default_token_generator.check_token(user, token):
            if password == re_password:
                user.set_password(password)
                user.save()
                return JsonResponse({
                            "massege": "ok",
                            })
        return JsonResponse({
                    "massege": "no",
                    })