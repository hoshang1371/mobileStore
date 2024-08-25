from rest_framework import serializers

from .models import OrderDetail,Order

from mobileStore_product.serializers import ProductDitailSerializer
from post_information.models import PaymentMethodeDetail,PostAddressDetail

from post_information.serializer import PaymentMethodeDetailSerializer,PostAddressDetailSerializer

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

class OrderDetilsFor_AllOrder(serializers.ModelSerializer):
    get_detail_sum = serializers.CharField()
    class Meta:
        model = OrderDetail
        # fields = '__all__'
        fields = (
                'count',
                'price',
                'get_detail_sum',
                  )
        # def to_representation(self, instance):
        #     result = super(OrderDetilsFor_AllOrder, self).to_representation(instance)
# PaymentMethodeDetail
class AllOrderProductSerializer(serializers.ModelSerializer):
    orderDetails = serializers.SerializerMethodField(read_only=True)
    # orderDetails = serializers.SerializerMethodField(read_only=True)
    PaymentMethode = serializers.SerializerMethodField(read_only=True)
    PostAddressDetail = serializers.SerializerMethodField(read_only=True)
    #PaymentMethodeDetailSerializer

    def get_orderDetails(self, obj):
        selected_options = OrderDetail.objects.filter(
            order=obj).distinct()
        return OrderDetilsFor_AllOrder(selected_options, many=True).data
    
    def get_PaymentMethode(self, obj):
        selected_options = PaymentMethodeDetail.objects.filter(
            OrderDetailSelected=obj).distinct()
        return PaymentMethodeDetailSerializer(selected_options, many=True).data
    
    def get_PostAddressDetail(self, obj):
        selected_options = PostAddressDetail.objects.filter(
            OrderDetailSelected=obj).distinct()
        return PostAddressDetailSerializer(selected_options, many=True).data
    
    class Meta:
        model = Order
        fields = (
        'id',
        'is_paid',
        'j_create_date',
        'j_payment_date',
        'is_send',
        'codeFolowed',
        'orderDetails',
        'PaymentMethode',
        'PostAddressDetail',
        )
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["get_All_detail_sum"] = sum([int(order["get_detail_sum"] )for order in representation['orderDetails']])
        return representation


