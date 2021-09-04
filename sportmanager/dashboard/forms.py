from django import forms
from authentication.models import User

team_choices = (('MASCHILE', 'MASCHILE'), ('FEMMINILE', 'FEMMINILE'),('MINIVOLLEY', 'MINIVOLLEY'))

class SearchForm(forms.Form):
    text = forms.CharField(label='Cerca', max_length=100, required=False)
    team = forms.ChoiceField(widget=forms.Select, choices=team_choices, required=False)
    