from django.urls import path, include

from . import views

urlpatterns = [
    path('sliderUp/',views.sliderUp.as_view()),
    path('sliderDown/',views.sliderDown.as_view()),
    ]