from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


@admin.register(VolleyCoach)
class UserAdmin(DjangoUserAdmin):
    exclude = ['role']


@admin.register(VolleyManager)
class UserAdmin(DjangoUserAdmin):
    exclude = ['role']

admin.site.register(VolleyGym)
admin.site.register(VolleyGymConf)

admin.site.register(VolleyTeam)
admin.site.register(VolleyMatch)

admin.site.register(VolleyReservation)
