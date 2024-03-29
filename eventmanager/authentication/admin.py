from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    exclude = ['role']

@admin.register(Customer)
class UserAdmin(DjangoUserAdmin):
    exclude = ['role']


admin.site.register(ThemeConfig)