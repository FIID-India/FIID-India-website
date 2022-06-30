from django import forms
from . import models


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
