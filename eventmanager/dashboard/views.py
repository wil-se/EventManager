from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentication.views import main_render
from reservation.models import Team, Match, Gym, Reservation
import datetime
from .forms import SearchForm


@login_required(login_url='/accounts/login/')
def dashboard(request):
    matches = Match.objects.all()
    print("hello")
    if request.GET.get('date',''):
        date = request.GET.get('date','')
        start_date = datetime.datetime.strptime(date.split(' - ')[0], '%d/%m/%Y')
        end_date = datetime.datetime.strptime(date.split(' - ')[1], '%d/%m/%Y')
    else:
        start_date = datetime.datetime.now()
        end_date = datetime.datetime.now()

    form_fields = {}
    form_fields['text'] = ''
    form_fields['team'] = ''
    form = SearchForm(request.GET or None, request.FILES or None, initial=form_fields)

        

    return main_render(request, page='dashboard.html', data={
        'matches':matches,
        'start_date': start_date.strftime('%d/%m/%Y'),
        'end_date': end_date.strftime('%d/%m/%Y'),
        'form': form,
        })