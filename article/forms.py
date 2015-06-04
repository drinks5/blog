#__author__ = 'drinksober`'
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField
    emai = forms.EmailField
    message = forms.CharField
