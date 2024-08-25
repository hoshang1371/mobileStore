from rest_framework import serializers

from .models import PaymentMethodeDetail,PostAddressDetail

class PostAddressDetailSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = PostAddressDetail
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
        )
        depth = 1