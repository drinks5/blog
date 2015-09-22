#__author__ = 'drinksober`'
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required = False, label=' e-mail address')
    message = forms.CharField(widget = forms.Textarea)
