from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from djoser import utils
from django.contrib.auth.tokens import default_token_generator
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import User
import datetime 
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics

from extentions.sendSmsRandom import random_with_N_digits,sendSmsForVarifyAddress,sendSms
# from django.contrib.auth.models import User
from .models import UserCodeVarify
# from django.core.exceptions import ObjectDoesNotExist

from .serializers import ChangePasswordSerializer
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
        # print("uid=",uid)
        # print("token=",token)
        # print(request.data)
        # print(request.data.get('password'))
        # print(request.data.get('re_password'))

        password= request.data.get('password')
        re_password= request.data.get('re_password')


        user = User.objects.filter(id=utils.decode_uid(uid))[0]
        # print(user)

        # print("default_token_generator=", default_token_generator.check_token(user, token))
        # print("==========================")
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
    
class sendCodeMobileNumber(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        u = Token.objects.get(pk=request.auth).user
        user = User.objects.filter(email=u)[0]
        mobileNumber = request.data.get('mobileNumber')


        if mobileNumber=='':
            # TODO : ارور برای وارد کردن شماره موبایل
            # messages.success(request, 'لطفاً شماره موبایل را وارد کنید.')
            # print("not ok")
            return JsonResponse({"mobNum": "not ok"})
        
        # user.codeVarifySms = random_with_N_digits(5)
        # user.codeVarifySmsDate = datetime.datetime.now(datetime.timezone.utc)
        # print(user.usercodevarify.codeVarifySms)
        # try:
        #          print(user.usercodevarify.codeVarifySms)
        # except ObjectDoesNotExist:
        code = UserCodeVarify.objects.filter(user=user)
        if code.exists():
            code.all().delete()


        co= UserCodeVarify.objects.create(
                user=user,
                codeVarifySms = random_with_N_digits(5),
                codeVarifySmsDate = datetime.datetime.now(datetime.timezone.utc)
                )
        user.save()
        sendSms(co.codeVarifySms,mobileNumber)
        return JsonResponse({
                    "massege": "ok",
                    })
    
class setMobileNumber(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        u = Token.objects.get(pk=request.auth).user
        user = User.objects.filter(email=u)[0]
        mobileNumber = request.data.get('mobileNumber')
        code = request.data.get('code')

        codeSaved = UserCodeVarify.objects.filter(user=user)
        deffTime =int(datetime.datetime.now(datetime.timezone.utc).timestamp()-codeSaved.first().codeVarifySmsDate.timestamp())
        if(deffTime < 120):
            #!
            user.mobile_phone_number = mobileNumber
            user.save()
            return JsonResponse({
                    "massege": "ok",
                    })
        

        return JsonResponse({
        "massege": "timeFin",
        })
    
class ChangePassword(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def put(self, request):
        u = Token.objects.get(pk=request.auth).user
        user = User.objects.filter(email=u)[0]
        password = request.data['password']
        new_password = request.data['new_password']

        if not user.check_password(raw_password=password):
            return Response({'error': 'password not match'}, status=400)
        else:
            user.set_password(new_password)
            user.save()
            return Response({'success': 'password changed successfully'}, status=200)
        

        # password = request.data['password']
        # new_password = request.data['new_password']

        # obj = get_user_model().objects.get(pk=id)
        # if not obj.check_password(raw_password=password):
        #     return Response({'error': 'password not match'}, status=400)
        # else:
        #     obj.set_password(new_password)
        #     obj.save()
        #     return Response({'success': 'password changed successfully'}, status=200)