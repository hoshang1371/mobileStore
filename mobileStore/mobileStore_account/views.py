from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate ,login

# class LoginView(APIView):
#     def post(self, request, format=None):
#         data = request.data

#         username = data.get('username', None)
#         password = data.get('password', None)

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             if user.is_active:
#                 login(request, user)

        #         return Response(status=status.HTTP_200_OK)
        #     else:
        #         return Response(status=status.HTTP_404_NOT_FOUND)
        # else:
        #     return Response(status=status.HTTP_404_NOT_FOUND)