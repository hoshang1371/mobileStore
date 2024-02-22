from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.Site_Setting.as_view()),
    ]