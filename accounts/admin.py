from django import forms
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from django.forms import CheckboxSelectMultiple
from django.db import models


class UserAdmin(CustomUserAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    list_display = ('email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'date_joined', 'last_login')}),
        ('Permissions', {'fields':('groups','is_staff', 'is_superuser')}),
    )
    readonly_fields=('date_joined', 'last_login', 'is_superuser')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name', 'last_name','password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)