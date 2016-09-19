

from django import forms
 
class ContactForm(forms.Form):
    
    city = forms.CharField()
    state_province = forms.CharField()
    country = forms.CharField()
    notes = forms.CharField()
    image = forms.FileField()
