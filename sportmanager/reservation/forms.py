from django import forms
from reservation.models import Seat

team_category_choices = (('MASCHILE', 'MASCHILE'), ('FEMMINILE', 'FEMMINILE'),('MINIVOLLEY', 'MINIVOLLEY'))

class SeatForm(forms.Form):
    seats = forms.ModelChoiceField(queryset=Seat.objects.all(), required=False)