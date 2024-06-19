from django.contrib import admin

from post_information.models import (
    # PostAddressDetail, 
    PostPrice,
    # PostAddress,
    # PaymentMethodeDetail
)

class PostPriceAdmin(admin.ModelAdmin):
    list_display = ['__str__','title', 'price']

admin.site.register(PostPrice,PostPriceAdmin)