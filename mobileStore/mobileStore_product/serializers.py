
from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField

import convert_numbers

from mobileStore_product_category.models import ProductCategory

from .models import CustomerComment, LikesCustomerComment, Product, ProductGallery,Rating,Likes

from mobileStore_product_category.serializers import ProductCategorySerializer



class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'


class LikesCustomerCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikesCustomerComment
        fields = '__all__'


class ProductDetailProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "code",
            "get_absolute_url",
            "description",
            "price",
            "priceOff",
            # "categories",
            "visit_count",
            "get_image",
            "int_average_rating",
            "float_average_rating",
            "get_thumbnail",
            "get_absolute_url",
            )


    # def get_parnt_category(self,serial,categ=[]):

    #     category = ProductCategory.objects.filter(pk=serial).first()

    #     if category.parent != None:
    #         cat = category.parent.id
    #         a ={
    #             "title":category.title,
    #             "link":category.name
    #         }
    #         categ.append(a)

    #         self.get_parnt_category(serial=cat,categ=categ)
    #     else:
    #         a ={
    #             "title":category.title,
    #             "link":category.name
    #         }
    #         categ.append(a)

    #     return(categ)

  
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['price'] = convert_numbers.english_to_persian(str(representation['price']))
        if representation['priceOff'] != None:
            representation['priceOff'] = convert_numbers.english_to_persian(str(representation['priceOff']))

        # cat = representation['categories'][0]

        # categories= self.get_parnt_category(cat)
        # print(f'categories={categories}')
        # # ProductCategory.objects.all()
        # representation['categories'] = categories
        return representation
    
class ProductDitailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "code",
            "get_absolute_url",
            "description",
            "price",
            "priceOff",
            "categories",
            "visit_count",
            "get_image",
            "int_average_rating",
            "float_average_rating",
            "get_thumbnail",
            "get_absolute_url",
            )


    def get_parnt_category(self,serial,categ=[]):

        category = ProductCategory.objects.filter(pk=serial).first()

        if category.parent != None:
            cat = category.parent.id
            a ={
                "title":category.title,
                "link":category.name
            }
            categ.append(a)

            self.get_parnt_category(serial=cat,categ=categ)
        else:
            a ={
                "title":category.title,
                "link":category.name
            }
            categ.append(a)
        # finalCat = categ
        # categ =[]
        return(categ)

  
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['price'] = convert_numbers.english_to_persian(str(representation['price']))
        if representation['priceOff'] != None:
            representation['priceOff'] = convert_numbers.english_to_persian(str(representation['priceOff']))

        cat = representation['categories'][0]

        categories= self.get_parnt_category(cat,categ=[])
        # print(f'categories={categories}')
        representation['categories'] = categories
        return representation
    

class DeleteCustomerCommentSerializer(serializers.ModelSerializer):
    model = CustomerComment
    fields = (
        "id",
        )





class CustomerCommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        time_calc = serializers.CharField(source='time_calc')
        like_comment_calc = serializers.CharField(source='like_comment_calc')
        # is_liked = serializers.CharField(source='is_liked')
        model = CustomerComment
        fields = (
            "id",
            "user",
            "text",
            "created",
            "updated",
            "time_calc",
            "like_comment_calc",
            # "is_liked",
            "parent",
            "replies",
        )
        depth = 1
        # fields = '__all__'

    def get_fields(self):
        fields = super(CustomerCommentSerializer, self).get_fields()
        fields['replies'] = CustomerCommentSerializer(many=True, read_only=True)
        return fields
    

class PostCustomerCommentSerializer(serializers.ModelSerializer):
    model = CustomerComment
    fields = (
        "user",
        "text",
        "CommentProduct",
        )
