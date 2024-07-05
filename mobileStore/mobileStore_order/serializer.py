from rest_framework import serializers

from .models import OrderDetail,Order

from mobileStore_product.serializers import ProductDitailSerializer
#! Order  OrderProductSerializer
class OrderProductSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source="user.username", read_only=True)
    product = ProductDitailSerializer(read_only=True)

    class Meta:
        model = OrderDetail
        fields = "__all__"
        depth = 1
        # fields = {'product','count'}

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # print(representation['count'])
        # print(representation['product']['number'])
        if(int(representation['count'])>int(representation['product']['number'])):
            representation['error'] = "این تعداد در انبار موجود نیست"
        else:
            representation['error'] =""
        return representation


class DeleteOrderDetailSerializer(serializers.ModelSerializer):
    model = OrderDetail
    fields = (
        "id",
        )
    
class OrderProductSerializerForListOfbuy(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        # fields = '__all__'
        fields = ('id','count')