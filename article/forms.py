#__author__ = 'drinksober`'
# coding=utf-8
from django import forms
from .models import Comment

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,help_text="test help")
    email = forms.EmailField(required = False, label=' e-mail address')
    message = forms.CharField(widget = forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'email', 'text', ]
        labels = {
            'author' : u'昵称',
            'email'  : u'电子邮箱',
            'text'   : u'评论内容',
        }
        widgets = {
            'text' : forms.Textarea(),
        }
