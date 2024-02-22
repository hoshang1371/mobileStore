from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import sliderUpSerializer,sliderDownSerializer

from .models import SliderUp,SliderDown

from rest_framework.response import Response

class sliderUp(APIView):
    def get(self, request, format=None):
        Slider_up = SliderUp.objects.all()[0:2]
        serializer = sliderUpSerializer(Slider_up, many=True)
        return Response(serializer.data)

class sliderDown(APIView):
    def get(self, request, format=None):
        Slider_down = SliderDown.objects.all()[0:2]
        serializer = sliderDownSerializer(Slider_down, many=True)
        return Response(serializer.data)