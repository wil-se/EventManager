from django import forms

class SearchForm(forms.Form):
    text = forms.CharField(label='Cerca', max_length=100, required=False)
    