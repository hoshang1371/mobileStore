from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from .models import UserCodeVarify
from django.contrib.auth import get_user_model

User = get_user_model()
# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         *UserAdmin.fieldsets,  # original form fieldsets, expanded
#         (                      # new fieldset added on to the bottom
#             'آخرین کد تایید پیامکی',  # group heading of your choice; set to None for a blank space instead of a header
#             {
#                 'fields': (
#                     'codeVarifySms',
#                     'codeVarifySmsDate',
#                 ),
#             },
#         ),
#     )

    
# admin.site.register(User, CustomUserAdmin)
admin.site.register(User)
admin.site.register(UserCodeVarify)