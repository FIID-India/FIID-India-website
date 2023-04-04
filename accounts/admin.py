from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils.translation import ugettext_lazy as _


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    fieldsets = (
        (_('User'), {'fields': ('first_name', 'last_name', 'email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    readonly_fields = ('date_joined', 'last_login')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ()
