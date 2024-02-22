from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import foundersSerializer
from .models import Founders
# Create your views here.
class Site_Founders(APIView):
    def get(self, request, format=None):
        site_founders = Founders.objects.all()
        serializer = foundersSerializer(site_founders, many=True)
        return Response(serializer.data)