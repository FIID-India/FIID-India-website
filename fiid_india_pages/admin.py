from django.contrib import admin
from .models import Page, Summary

class SummaryTabularInline(admin.TabularInline):
    model = Summary

class PageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields=('name',)
    inlines = [SummaryTabularInline]

    class Meta:
        model = Page

admin.site.register(Page, PageAdmin)