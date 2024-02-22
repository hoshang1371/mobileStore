from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
User = get_user_model()

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.models import TokenUser

# class TokenStrategy:
#     @classmethod
#     def obtain(cls, user):
#         print("kir khar")
#         u = User.objects.get(id=user.id) 
#         token=Token.objects.create(user=u) 
#         return {
#             "token": "1234567",
#             "user": user,
#         }

# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token


# class TokenStrategy:

#     @classmethod
#     def obtain(cls, user):
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})

class TokenStrategy:
    @classmethod
    def obtain(cls, user):
        from rest_framework_simplejwt.tokens import RefreshToken
        refresh = RefreshToken.for_user(user)
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": user,
        }
