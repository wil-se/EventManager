from authentication.views import main_render
from .models import Match, Reservation
from django.http import JsonResponse
from django.http import HttpResponse



def reservation(request):
    return main_render(request, 'reservation.html', {})


def match(request, id):
    match = Match.objects.get(pk=id)
    reservations = Reservation.objects.filter(match=match)
    # free_seats = match.gym.seats - len(reservations)
    free_seats = len(match.get_free_seats())
    return main_render(request, 'match.html', {
        'match':match,
        'free_seats': free_seats,
        })

def reserve_match(request, id):
    match = Match.objects.get(pk=id)
    reservations = Reservation.objects.filter(match=match)
    free_seats = len(match.get_free_seats())
    return main_render(request, 'reserve_match.html', {
        'match':match,
        'free_seats': free_seats,
        })

def save_reservation(request):
    id = request.POST.get('id', None)
    if not id:
        return HttpResponse(status=500)
    
    match = Match.objects.get(pk=id)
    reservations = Reservation.objects.filter(match=match)
    
    print(reservations)
    free_seats = len(match.get_free_seats())
    if free_seats <= 0:
        return HttpResponse(status=500)
    
    reservation = Reservation()
    reservation.user = request.user
    reservation.match = match
    reservation.seat = match.get_free_seats()[0]
    reservation.save()

    print(reservation)

    return main_render(request, 'reserve_match.html', {
        'match':match,
        'free_seats': free_seats,
        })

def save_seats(request):
    
    return main_render(request, 'profile.html', {
        })

