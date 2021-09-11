from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    path('profilo', profile, name='profilo'),
    path('get-gym-config', get_gym_config, name='get-gym-config'),
    path('set-gym-config', set_gym_config, name='set-gym-config'),
       
]
