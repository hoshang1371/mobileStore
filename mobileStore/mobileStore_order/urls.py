from django.urls import path, include

# from mobileStore.mobileStore_order.views import product_order
from .views import product_order,DeleteOrderDetail,product_order_List_buy,\
                    product_orders_details_List_buy,All_product_order,product_order_by_id,\
                    NoPey_product_order

urlpatterns = [
    #!product order url
    path('product_order/', product_order.as_view()),
    path('Delete_product_orderDetail/<int:pk>/',DeleteOrderDetail.as_view()),
    path('update_for_buy/', product_order_List_buy.as_view() ,name="UpdateForBuyList"),
    path(
        'product_orders_details_List_buy/', 
        product_orders_details_List_buy.as_view() 
        ,name="product_orders_details_List_buy"),
    path('All_product_order/', All_product_order.as_view()),
    path('NoPey_product_order/', NoPey_product_order.as_view()),
    path('product_order_by_id/<int:id>/',product_order_by_id.as_view()),
]