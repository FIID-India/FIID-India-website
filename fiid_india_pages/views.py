from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from . import forms
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .email import ContactEmail
from django.views import generic


# Home Page View
class HomePageView(generic.TemplateView):
    template_name = 'fiid_india_pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {}
        context["about_images"] = models.Image.objects.filter(
            page="About").order_by('-id')[:1]
        context["programmes_images"] = models.Image.objects.filter(
            page="Programmes").order_by('-id')[:1]
        context["objectives_images"] = models.Image.objects.filter(
            page="Objectives").order_by('-id')[:1]
        context["carousel"] = models.Carousel.objects.all().order_by('-id')[:3]
        return context


# About Page View
class AboutPageView(generic.TemplateView):
    template_name = 'fiid_india_pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {}
        context["about_images"] = models.Image.objects.filter(
            page="About").order_by('-id')[:3]
        return context


# Programmes Page View
class ProgrammesPageView(generic.TemplateView):
    template_name = "fiid_india_pages/programmes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {}
        context["programmes_images"] = models.Image.objects.filter(
            page="Programmes").order_by('-id')[:3]
        return context


# Objectives Page View
class ObjectivesPageView(generic.TemplateView):
    template_name = 'fiid_india_pages/objectives.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {}
        context["objectives_images"] = models.Image.objects.filter(
            page="Objectives").order_by('-id')[:3]
        return context


# Contact Page View
class ContactPageView(generic.CreateView):
    model = models.Contact
    template_name = 'fiid_india_pages/contact.html'
    form_class = forms.ContactForm

    def form_valid(self, form):
        full_name = form.cleaned_data['full_name']
        sender_email_id = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        # Send email
        ContactEmail(full_name, sender_email_id,
                     subject, message).send_to_admin()

        # Display success message
        message = "Thankyou for contacting us!! We will get back to you soon"
        messages.success(self.request, message)

        return super(ContactPageView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('fiid-india-pages:contact-page')


# File Page View
class FilesPageView(generic.ListView):
    model = models.File
    context_object_name = 'files'
    template_name = 'fiid_india_pages/files.html'
    ordering = ['-id']


# Galary View
class GallaryPageView(generic.ListView):
    model = models.Image
    context_object_name = 'images'
    template_name = 'fiid_india_pages/gallary.html'
    ordering = ['-id']
