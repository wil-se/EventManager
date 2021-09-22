from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    path('profilo', profile, name='profile'),
    path('get-canvas-config', get_canvas_config, name='get-canvas-config'),
    path('set-canvas-config', set_canvas_config, name='set-canvas-config'),
    path('save-user', save_user, name='save_user'),
    path('add-user', add_user, name='add_user'),
    
]
