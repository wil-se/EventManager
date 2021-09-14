from django.contrib import admin
from .models import User, ThemeConfig, GymConfig

# Register your models here.
admin.site.register(User)
admin.site.register(ThemeConfig)
admin.site.register(GymConfig)
