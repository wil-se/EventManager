from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    path('overview', overview, name='overview'),
    path('', overview, name='overview'),
    path('my-reservations', my_reservations, name='my_reservations'),
]
