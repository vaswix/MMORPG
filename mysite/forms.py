from django import forms

from mysite.models import Advert, Reply


class AdvertCreationForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ['title', 'text', 'image', 'category']


class ReplyCreationForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']
