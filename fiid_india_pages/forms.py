from dataclasses import fields
from django import forms
from . import models

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = models.Subscriber
        fields = [
            'full_name',
            'email',
        ]

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = [
            'full_name',
            'email',
            'subject',
            'message',
        ]