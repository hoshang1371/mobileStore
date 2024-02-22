from rest_framework import serializers

from .models import news

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = '__all__'