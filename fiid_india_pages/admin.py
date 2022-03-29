from django.contrib import admin
from .models import (
    Page, Summary, Paragraph,
    Carousel, Image, Address,
    Contact, Newsletter, Reports,
    NewslettersAndReports, Subscriber
    )

class SummaryStackedInline(admin.StackedInline):
    model = Summary

class ParagraphStackedInline(admin.StackedInline):
    model = Paragraph

class ImageStackedInline(admin.StackedInline):
    model = Image

class NewsletterStackedInline(admin.StackedInline):
    model = Newsletter

class ReportStackedInline(admin.StackedInline):
    model = Reports

class PageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields=('name',)
    inlines = [SummaryStackedInline, ParagraphStackedInline, ImageStackedInline]

    class Meta:
        model = Page

class NewslettersAndReportsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_and_time')
    search_fields = ('title',)
    inlines = [NewsletterStackedInline, ReportStackedInline]

    class Meta:
        model = NewslettersAndReports

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('heading',)
    search_fields = ('heading',)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('page',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'date_and_time')
    search_fields = ('full_name', 'email')

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')
    search_fields = ('full_name', 'email')


admin.site.register(Page, PageAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(NewslettersAndReports, NewslettersAndReportsAdmin)
admin.site.register(Subscriber, SubscriberAdmin)