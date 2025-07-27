from django import forms 

from .models import App

from django import forms

class ChaiVarietyForm(forms.Form):
    
  
    chai_variety=forms.ModelChoiceField(queryset=App.objects.all(),
                                       label="Select chai quality" )
    