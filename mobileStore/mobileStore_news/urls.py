from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.Site_News.as_view()),
    ]