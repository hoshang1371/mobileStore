from django.contrib import admin

from post_information.models import (
    PostPrice,
    PostAddress,
    PaymentMethodeDetail,
    PostAddressDetail
)

class PostPriceAdmin(admin.ModelAdmin):
    list_display = ['__str__','title', 'price']

admin.site.register(PostPrice,PostPriceAdmin)
admin.site.register(PaymentMethodeDetail)
admin.site.register(PostAddressDetail)
admin.site.register(PostAddress)