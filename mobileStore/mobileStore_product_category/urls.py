from django.urls import path, include

from . import views


urlpatterns = [
    path('ProductDetailProductGallery/<slug:product_id>',views.ProductDetailProductGallery.as_view()),

]