from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializers import ProductCategorySerializer
from .models import ProductCategory
class ProductDetailProductGallery(ListAPIView):
        queryset = ProductCategory.objects.all()
        serializer_class = ProductCategorySerializer
        model = serializer_class.Meta.model
        
        # def get_queryset(self):
        #     product_id = self.kwargs['product_id']
        #     queryset = self.model.objects.filter(product_id=product_id)
            # return Response({"message": "product is added"})

            # return queryset