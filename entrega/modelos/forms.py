from django import forms

class JugadoresForm(forms.Form):
    name = forms.CharField(max_length= 50)
    price = forms.FloatField()
  