from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    path('volley', volley, name='volley'),
    path('volley-match/<int:id>', volley_match, name='volley_match'),
    path('get-match-data', get_match_data, name='get_match_data'),
    path('reserve-volley-match', reserve_volley_match, name='reserve_volley_match'),
    
]
