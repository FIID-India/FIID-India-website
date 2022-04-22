import email
from django.db import models
from django.contrib.auth.models import AbstractUser
from . userManager import UserManager
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
