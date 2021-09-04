from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    path('profilo', profile, name='profilo'),
]
