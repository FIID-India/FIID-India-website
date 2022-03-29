from operator import mod
from pyexpat import model
from re import search
from django.contrib import admin
from .models import Page, Summary, Paragraph, Carousel, Image, Address, Contact

class SummaryTabularInline(admin.TabularInline):
    model = Summary

class ParagraphTabularInline(admin.TabularInline):
    model = Paragraph

class ImageTabularInline(admin.TabularInline):
    model = Image

class PageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields=('name',)
    inlines = [SummaryTabularInline, ParagraphTabularInline, ImageTabularInline]

    class Meta:
        model = Page

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('heading',)
    search_fields = ('heading',)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('page',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'date_and_time')
    search_fields = ('full_name', 'email')

admin.site.register(Page, PageAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Contact, ContactAdmin)