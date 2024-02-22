from django.contrib.auth.models import User


from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'id',
        'username',
        'password',
        'is_active',
        "email"
        )