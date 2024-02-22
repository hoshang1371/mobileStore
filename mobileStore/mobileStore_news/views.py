from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import NewsSerializer
from .models import news
# Create your views here.
class Site_News(APIView):
    def get(self, request, format=None):
        site_news = news.objects.all()
        serializer = NewsSerializer(site_news, many=True)
        return Response(serializer.data)