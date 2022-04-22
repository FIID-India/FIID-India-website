from dataclasses import fields
from django import forms
from . import models


# Subscriber Form
class SubscribeForm(forms.ModelForm):
    class Meta:
        model = models.Subscriber
        fields = [
            'full_name',
            'email',
        ]


# Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = [
            'full_name',
            'email',
            'subject',
            'message',
        ]
