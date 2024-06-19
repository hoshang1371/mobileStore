from django.urls import path, include

# from mobileStore.mobileStore_order.views import product_order
from .views import product_order,DeleteOrderDetail,product_order_List_buy

urlpatterns = [
    #!product order url
    path('product_order/', product_order.as_view()),
    path('Delete_product_orderDetail/<int:pk>/',DeleteOrderDetail.as_view()),
    path('update_for_buy/', product_order_List_buy.as_view() ,name="UpdateForBuyList"),
]