from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    path('', dashboard, name='dashboard'),
]
