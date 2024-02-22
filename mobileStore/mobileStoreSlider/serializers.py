from rest_framework import serializers

from .models import SliderUp,SliderDown

class sliderUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderUp
        fields = (
            "id",
            'title',
            'link',
            'description1',
            'description2',
            'imageSlider',
            'get_image_sliderUp',
        )

class sliderDownSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderDown
        fields = (
            "title",
            "link",
            "description1",
            "imageSlider",
            "get_image_SliderDown",
        )