from django.urls import path, include

from . import views

urlpatterns = [
    path('activate/<uid>/<token>/',views.finishActiveEmail.as_view()),
    path('password/reset/confirm/<uid>/<token>/',views.finishForgetPass.as_view()),
    #!
    path('api/v1/sendCodeMobileNumber/',views.sendCodeMobileNumber.as_view()),
    path('api/v1/setMobileNumber/',views.setMobileNumber.as_view()),
    ]