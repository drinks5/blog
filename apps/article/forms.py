# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-03-09 13:14:06
# @Last Modified by:   drinks
# @Last Modified time: 2016-03-09 17:47:31
from django import forms
from .models import Comment


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, help_text="test help")
    email = forms.EmailField(required=False, label=' e-mail address')
    message = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', ]
        labels = {
            'text': u'评论内容',
        }
        widgets = {
            'text': forms.Textarea(),
        }
