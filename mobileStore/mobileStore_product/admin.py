from django.contrib import admin

from audioop import reverse
from django.contrib import admin

# Register your models here.
from .models import Product ,ProductGallery, Likes,Rating, CustomerComment, LikesCustomerComment

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active']

    class Meta:
        model = Product


@admin.register(CustomerComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'CommentProduct', 'created', 'is_ok')
    list_filter = ('is_ok', 'created', 'updated')
    search_fields = ('user', 'text')


@admin.register(LikesCustomerComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'CustomerComment', 'likes')
    list_filter = ('user', 'CustomerComment', 'likes')
    search_fields = ('user', 'CustomerComment','likes')


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductGallery)

admin.site.register(Likes)

admin.site.register(Rating)

# admin.site.register(LikesCustomerComment)