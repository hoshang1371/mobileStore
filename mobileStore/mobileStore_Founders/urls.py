from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.Site_Founders.as_view()),
    ]