from django import forms
from . import models

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = models.Subscriber
        fields = [
            'full_name',
            'email',
        ]