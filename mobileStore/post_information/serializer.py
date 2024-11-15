from rest_framework import serializers

from .models import PaymentMethodeDetail,PostAddressDetail,PostPrice,PostAddress

class PostAddressDetailSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = PostAddressDetail
            fields = "__all__"
            


class PostAddressDetailSerializer_for_Peyment(serializers.ModelSerializer):
        
        class Meta:
            model = PostAddressDetail
            fields = "__all__"
            depth =1
class PostPriceSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = PostPrice
            fields = "__all__"


class PaymentMethodeDetailSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source="user.username", read_only=True)
    PaymentDetails = serializers.CharField(source='get_PaymentDetails_display')

    # def get_PaymentDetails(self,obj):
    #     return obj.get_PaymentDetails_display()
    
    class Meta:
        model = PaymentMethodeDetail
        # fields = "__all__"
        fields = (
            'PaymentDetails',
            'isTermsAndRules',
            'peymentCode',
            'peymentDate',
        )
        depth = 1


class PostAddressSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = PostAddress
            # fields = "__all__"
            fields = (
                  'address',
                'post_code'
            )

class PaymentMethodeDetailSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = PaymentMethodeDetail
            fields = "__all__"