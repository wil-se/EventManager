from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import ThemeConfig
from reservation.models import Reservation
from reservation.forms import SeatForm

@login_required(login_url='/accounts/login/')
def main_render(request, page='dashboard.html', data={}):
    themeconfig = ThemeConfig.objects.filter(user=request.user)[0]
    print(themeconfig.navbar)
    return render(request, page, {**{
        'theme': themeconfig,
    }, **data})

@login_required(login_url='/accounts/login/')
def profile(request):
    reservations = Reservation.objects.filter(user=request.user)
    seatform = SeatForm()
    
    return main_render(request, page="profile.html", data={
        'reservations': reservations,
        'seatform': seatform,
    })