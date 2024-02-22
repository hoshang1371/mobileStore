from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SiteSettingSerializer
from .models import SiteSetting
# Create your views here.
class Site_Setting(APIView):
    def get(self, request, format=None):
        setting = SiteSetting.objects.all().first()
        serializer = SiteSettingSerializer(setting)
        return Response(serializer.data)