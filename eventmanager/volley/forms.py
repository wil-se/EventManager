from django import forms


team_category_choices = (('MASCHILE', 'MASCHILE'), ('FEMMINILE', 'FEMMINILE'),('MINIVOLLEY', 'MINIVOLLEY'))

class SearchForm(forms.Form):
    text = forms.CharField(label='Cerca', max_length=100, required=False)
    team = forms.ChoiceField(widget=forms.Select, choices=team_category_choices, required=False)
    