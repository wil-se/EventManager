from django.shortcuts import render
import datetime
from .forms import SearchForm
from django.contrib.auth.decorators import login_required
from authentication.views import main_render
from .models import VolleyMatch


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