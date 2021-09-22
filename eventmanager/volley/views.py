from django.shortcuts import render
import datetime
from .forms import SearchForm
from django.contrib.auth.decorators import login_required
from authentication.views import main_render
from .models import *
from django.http import JsonResponse
from reservation.models import *



@login_required(login_url='/accounts/login/')
def volley(request):
    if request.GET.get('date',''):
        date = request.GET.get('date','')
        start_date = datetime.datetime.strptime(date.split(' - ')[0], '%d/%m/%Y')
        end_date = datetime.datetime.strptime(date.split(' - ')[1], '%d/%m/%Y')
    else:
        start_date = datetime.datetime.now()
        end_date = datetime.datetime.now()

    matches = VolleyMatch.objects.all()

    form_fields = {}
    form_fields['text'] = ''
    form_fields['team'] = ''
    form = SearchForm(request.GET or None, request.FILES or None, initial=form_fields)

        

    return main_render(request, page='volley.html', data={
        'start_date': start_date.strftime('%d/%m/%Y'),
        'end_date': end_date.strftime('%d/%m/%Y'),
        'form': form,
        'matches': matches,
        })



@login_required(login_url='/accounts/login/')
def volley_match(request, id):
    match = VolleyMatch.objects.get(pk=id)
    return main_render(request, 'volley_match.html', {
        'match':match,
        'free_seats': 0,
        })


@login_required(login_url='/accounts/login/')
def get_match_data(request):
    match_id = request.GET.get('match_id', None)
    match = VolleyMatch.objects.get(pk=match_id)
    reservations = VolleyReservation.objects.filter(event=match)
    canvas = Canvas.objects.filter(placeconfig=match.placeconfig).first()
    seatconfig = SeatCanvasConfig.objects.filter(canvas=canvas)
    shapes = Shape.objects.filter(canvas=canvas)
    
    data = {
        'free_seats': {},
        'reserved_seats': {},
        'shapes': {},
    }

    for s in seatconfig:
        print(s.seat.top)
        print(s.seat.left)
        
        if s.seat.pk not in reservations.values_list('seat', flat=True):
            data['free_seats'][s.seat.pk] = [s.seat.name, s.left, s.top, s.seat.radius]
        else:
            data['reserved_seats'][s.seat.pk] = [s.seat.name, s.left, s.top, s.seat.radius]
    
    for shape in shapes:
        data['shapes'][shape.pk] = [shape.name, shape.left, shape.top, shape.width, shape.height]

    data['canvas_width'] = canvas.width
    data['canvas_height'] = canvas.height

    return JsonResponse(data)


@login_required(login_url='/accounts/login/')
def reserve_volley_match(request):
    seat_id = request.POST.get('seat_id', None)
    match_id = request.POST.get('match_id', None)
    
    seat = Seat.objects.get(pk=seat_id)
    match = VolleyMatch.objects.get(pk=match_id)
    reservation = VolleyReservation.objects.filter(event=match, seat=seat)
    
    print(request.user.pk)
    customer = Customer.objects.get(pk=request.user.pk)

    if not reservation:
        reservation = VolleyReservation()
        reservation.customer = customer
        reservation.event = match
        reservation.seat = seat
        reservation.save()

    print(reservation)
    
    print(seat_id)
    print(match_id)


    return JsonResponse({})