from django.urls import path, include


from .views import (
    PostAddressDetail_selected,
    PostAddressDetail_peyment,
    PaymentMethodeDetail_peyment,
    # PostAddress_get
    )

urlpatterns = [
    #!product order url
    path('PostAddressDetail_selected/<int:id>/', PostAddressDetail_selected.as_view()),
    path('PostAddressDetail_peyment/<int:id>/', PostAddressDetail_peyment.as_view()),
    path('PaymentMethodeDetail_peyment/<int:id>/', PaymentMethodeDetail_peyment.as_view()),
    # path('PostAddress_get/', PostAddress_get.as_view()),
]