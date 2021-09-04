from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    path('eventi', reservation, name='eventi'),
    path('partita/<int:id>', match, name='partita'),
    path('partita/<int:id>/prenotazione', reserve_match, name='prenotazione_partita'),
    path('partita/effettua-prenotazione', save_reservation, name='effettua_prenotazione_partita'),
]
