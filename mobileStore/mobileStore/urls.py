"""
URL configuration for mobileStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenBlacklistView
# from rest_framework_simplejwt.views import (
#     TokenObtainSlidingView,
#     TokenRefreshSlidingView,
# )
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/',include('djoser.urls')),
    path('api/v1/',include('djoser.urls.authtoken')),
    # path("api/v1/", include("djoser.urls.jwt")),
    path("api/v1/", include("djoser.social.urls")),
    #?
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    
    #?

    path('api-auth/', include('rest_framework.urls')),

    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    # path('apio/token/', TokenObtainSlidingView.as_view(), name='token_obtain'),
    # path('apio/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    # path("auth/", include("djoser.urls")),
    # path("auth/", include("djoser.urls.jwt")),
    # path("auth/", include("djoser.urls")),
    # path("auth/", include("djoser.urls.jwt")),
    # path("auth/", include("djoser.social.urls")),
    # path("auth/", include("djoser.urls")),
    # path("auth/", include("djoser.urls.jwt")),
    # path("auth/", include("djoser.social.urls")),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    path('api/v1/',include('mobileStore_product.urls')),
    path('api/v1/',include('mobileStore_product_category.urls')),
    path('slider/',include('mobileStoreSlider.urls')),
    path('site__Setting/',include('mobileStore_settings.urls')),

    path('news/',include('mobileStore_news.urls')),
    path('founders/',include('mobileStore_Founders.urls')),
    path('',include('account.urls')),
    path('order/',include('mobileStore_order.urls')),
    path('post_information/',include('post_information.urls')),
    # path('',include('mobileStore_Social.urls')),
    # path("api/", include("mobileStore_Social.urls")),
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

