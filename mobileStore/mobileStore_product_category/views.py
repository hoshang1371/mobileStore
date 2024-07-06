from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

# from mobileStore.mobileStore_product.models import Product
from mobileStore_product.models import Product

from mobileStore_product.serializers import ProductSerializer

from .serializers import ProductCategorySerializer
from .models import ProductCategory

from rest_framework.decorators import api_view

class ProductDetailProductGallery(ListAPIView):
        queryset = ProductCategory.objects.all()
        serializer_class = ProductCategorySerializer
        model = serializer_class.Meta.model
        
        # def get_queryset(self):
        #     product_id = self.kwargs['product_id']
        #     queryset = self.model.objects.filter(product_id=product_id)
            # return Response({"message": "product is added"})

            # return queryset



@api_view(['POST'])
def category(request):
        query = request.data.get('query','')
        print(query)
        if query:
            products = Product.objects.filter(categories__title= query)
            # categ = products.first().productcategory_set.filter(id=1)
            print(products)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response({"products":[]})