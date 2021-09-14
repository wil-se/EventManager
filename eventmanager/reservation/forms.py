from django import forms
from reservation.models import Seat

team_category_choices = (('MASCHILE', 'MASCHILE'), ('FEMMINILE', 'FEMMINILE'),('MINIVOLLEY', 'MINIVOLLEY'))

class SeatForm(forms.Form):
    seats = forms.ModelChoiceField(queryset=Seat.objects.all(), required=False)
    width_space = forms.IntegerField()
    height_space = forms.IntegerField()
    width_field = forms.IntegerField()
    height_field = forms.IntegerField()
    
    seat_radius = forms.IntegerField()
