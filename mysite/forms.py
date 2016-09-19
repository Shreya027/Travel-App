

from django import forms
 
class ContactForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField()
    notes = forms.CharField()
    image = forms.FileField()


class ListForm(forms.Form):
    destination = forms.CharField(initial='')
   

