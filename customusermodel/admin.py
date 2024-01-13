from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.

class customuseradmin(UserAdmin):
    model=models.customuser
    list_display=['id','email','firstname','lastname','DOB','is_staff','is_superuser','is_active']
    list_display_links=['email']
    ordering=['date_joined']
    # search_fields=['email','firstname','lastname']
    # fieldsets = (
    #     (
    #         ("Login Credentials"), {
    #             "fields": ("email", "password",)
    #         }, 
    #     ),
    #     (
    #         ("Personal Information"),
    #         {
    #             "fields": ('firstname', 'lastname',)
    #         },
    #     ),
    #     (
    #         ("Permissions and Groups"),
    #         {
    #             "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
    #         },
    #     ),
    #     (
    #         ("Important Dates"),
    #         {
    #             "fields": ()
    #         },
    #     ),
    # )
    # add_fieldsets = (
    #         (None, {
    #             "classes": ("wide",),
    #             "fields": ("email", "firstname", "lastname", "password1", "password2", "is_staff", "is_active"),
    #         },),
    #     )


admin.site.register(models.customuser,customuseradmin)

