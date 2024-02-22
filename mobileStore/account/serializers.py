from rest_framework import serializers

from djoser.serializers import UserCreateSerializer as BaseCreateSerializer,UserSerializer as BaseUserSerializer#

from django.contrib.auth import get_user_model

User = get_user_model()

# UserCreateSerializer =BaseCreateSerializer
UserSerializer =BaseUserSerializer
# class UserCreateSerializer(BaseCreateSerializer):
#     class Meta(BaseCreateSerializer.Meta):
#         fields = ['id','username','password','is_active',"email"]

class UserCreateSerializer(BaseCreateSerializer):

    """Serializer for creating user."""

    class Meta(BaseCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "username","first_name","last_name","password")
