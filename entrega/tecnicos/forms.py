from django import forms

class TecnicosForm(forms.Form):
    name = forms.CharField(max_length= 50)
    club = forms.CharField(max_length= 50)
   