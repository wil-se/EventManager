from django.shortcuts import render
from django.http import JsonResponse

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import ThemeConfig, GymConfig
from reservation.models import Reservation, SeatGymConfig, Seat
from reservation.forms import SeatForm

import json


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
    gymconfig = GymConfig.objects.all().first()

    return main_render(request, page="profile.html", data={
        'reservations': reservations,
        'seatform': seatform,
        'gymconfig': gymconfig,
    })


@login_required(login_url='/accounts/login/')
def get_gym_config(request):
    # gymconfig = GymConfig.objects.get(pk=request.POST.get('gymconfigid', ''))
    gymconfig = GymConfig.objects.all().first()
    seatconfig = SeatGymConfig.objects.filter(gym=gymconfig)


    data = {'seats':{}}
    data['width_space'] = gymconfig.width_space
    data['height_space'] = gymconfig.height_space
    data['width_field'] = gymconfig.width_field
    data['height_field'] = gymconfig.height_field
    data['seat_radius'] = gymconfig.seat_radius
    data['left_field'] = gymconfig.left_field
    data['top_field'] = gymconfig.top_field
    

    for seat in seatconfig:
        print(seat.pk)
        print(seat)
        data['seats'][seat.seat.name] = [seat.left, seat.top]

    return JsonResponse(data)

@login_required(login_url='/accounts/login/')
def set_gym_config(request):
    # id = request.data.get('id', None)
    data = json.loads(list(request.POST.keys())[0])

    gymconfig = GymConfig.objects.all().first()
    gymconfig.width_space = data.get('width_space', 1600)
    gymconfig.height_space = data.get('height_space', 800)
    gymconfig.width_field = data.get('width_field', 800)
    gymconfig.height_field = data.get('height_field', 400)
    gymconfig.seat_radius = data.get('seat_radius', 60)
    
    gymconfig.left_field = data.get('left_field', 200)
    gymconfig.top_field = data.get('top_field', 200)
    
    gymconfig.save()

    for seatid in data['seats'].keys():
        seatconf = SeatGymConfig.objects.filter(gym=gymconfig, seat__pk=seatid).first()
        
        if not seatconf:
            seatconf = SeatGymConfig()
            seat = Seat.objects.get(pk=seatid)
            seatconf.seat = seat
            seatconf.gym = gymconfig

        seatconf.left = data['seats'][seatid][0]
        seatconf.top = data['seats'][seatid][1]
        seatconf.save()
        
    return JsonResponse({})