from django import forms

class ClubesForm(forms.Form):
    name = forms.CharField(max_length= 50)
    fundacion = forms.FloatField()