from django.contrib import admin
from .models import Page, Summary, Paragraph

class SummaryTabularInline(admin.TabularInline):
    model = Summary

class ParagraphTabularInline(admin.TabularInline):
    model = Paragraph

class PageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields=('name',)
    inlines = [SummaryTabularInline, ParagraphTabularInline]

    class Meta:
        model = Page

admin.site.register(Page, PageAdmin)