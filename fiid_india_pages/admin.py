from django.contrib import admin
from .models import (
    Carousel, Image,
    Contact, File
)


class ImageStackedInline(admin.StackedInline):
    model = Image


class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_and_time')
    search_fields = ('title',)


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('heading',)
    search_fields = ('heading',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'date_and_time')
    search_fields = ('full_name', 'email')


admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Image)
