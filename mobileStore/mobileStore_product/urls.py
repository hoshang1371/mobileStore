from django.urls import path, include

from . import views

urlpatterns = [
    path('latest-product/',views.LatestProductsList.as_view()),
    path('all-product/',views.AllProductsList.as_view()),
    path('PopularProductsList/',views.PopularProductsList.as_view()),
    path('vigeProductsList/',views.PopularVigeList.as_view()),
    # path('products/<slug:product_id>/<slug:product_title>',views.ProductDetail.as_view()),
    path('products/<slug:product_id>',views.ProductDetail.as_view()),
    path('priceOffList/',views.priceOffList.as_view()),
    path('SetStar/',views.SetStar),
    path('SetStarClass/',views.SetStarClass.as_view()),
    path('GetLikeClass/<slug:product_id>',views.LikeStarClass.as_view()),
    path('GetLikesCustomerComment/<slug:CustomerComment_id>',views.LikesCustomerCommentClass.as_view()),
    path('GetProductDetailProductGallery/<slug:product_id>',views.ProductDetailProductGallery.as_view()),
    path('GetCustomerComment/<slug:product_id>',views.CustomerCommentClass.as_view()),
    path('DeleteCustomerComment/<int:pk>/',views.DeleteCustomerComment.as_view()),
    path('PostCustomerComment/',views.PostCustomerComment.as_view()),
    path('GetAllProductCustomerComment/',views.AllProductCustomerCommentClass.as_view()),

    path("products/search/", views.search),

    ]