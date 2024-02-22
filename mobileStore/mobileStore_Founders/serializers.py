from rest_framework import serializers

from .models import Founders

class foundersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founders
        # fields = '__all__'
        fields = (
            "user",
            "title",
            "position",
            "description",
            "get_image",
        )