from django import forms
from reservation.models import Seat, Canvas, Shape

team_category_choices = (('MASCHILE', 'MASCHILE'), ('FEMMINILE', 'FEMMINILE'),('MINIVOLLEY', 'MINIVOLLEY'))

class SeatForm(forms.Form):
    seats = forms.ModelChoiceField(queryset=Seat.objects.all(), required=False)
    canvases = forms.ModelChoiceField(queryset=Canvas.objects.all(), required=False)
    shapes = forms.ModelChoiceField(queryset=Shape.objects.all(), required=False)
    canvas_width = forms.IntegerField()
    canvas_height = forms.IntegerField()    
    seat_radius = forms.IntegerField()
