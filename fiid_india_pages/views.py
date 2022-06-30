from django.conf import settings
from django.shortcuts import render
from . import models
from . import forms
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from . send_email import contact_email
from django.views import generic


# Home Page View

class HomePageView(generic.TemplateView):
    template_name = 'fiid_india_pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {}
        context["about_images"] = models.Image.objects.filter(page="About").order_by('-id')[:1]
        context["programmes_images"] = models.Image.objects.filter(page="Programmes").order_by('-id')[:1]
        context["objectives_images"] = models.Image.objects.filter(page="Objectives").order_by('-id')[:1]
        context["carousel"] = models.Carousel.objects.all().order_by('-id')[:3]
        return context
    

# About Page View
def about_page_view(request):
    context = {}
    try:
        context["about_images"] = models.Image.objects.filter(page="About").order_by('-id')[:3]
    except ObjectDoesNotExist:
        pass
    return render(request, "fiid_india_pages/about.html", context)


# Programmes Page View
def programmes_page_view(request):
    context = {}
    try:
        context["programmes_images"] = models.Image.objects.filter(page="Programmes").order_by('-id')[:3]
    except ObjectDoesNotExist:
        pass
    return render(request, "fiid_india_pages/programmes.html", context)


# Objectives Page View
def objectives_page_view(request):
    context = {}
    try:
        context["objectives_images"] = models.Image.objects.filter(page="Objectives").order_by('-id')[:3]
    except ObjectDoesNotExist:
        pass
    return render(request, "fiid_india_pages/objectives.html", context)


# Contact Page View
def contact_page_view(request):
    form = forms.ContactForm()
    context = {}
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():

            full_name = request.POST['full_name']
            subject = request.POST['subject']
            email = request.POST['email']
            message_send = request.POST['message']
            form.save()
            form = forms.ContactForm()
            recipients = [settings.EMAIL_HOST_USER, ]
            contact_email(full_name, message_send, recipients,
                          email, subject, 'contact_recive.html')

            message = "Thankyou for contacting us!! We will get back to you soon"
            messages.success(request, message)
        else:
            for field, errors in form.errors.items():
                error = '{}'.format(''.join(errors))
                messages.error(request, error)

    context["form"] = form
    return render(request, "fiid_india_pages/contact.html", context)


# File Page View
def file_page_view(request):
    context = {}
    files = models.File.objects.all().order_by('-id')
    context["files"] = files
    return render(request, "fiid_india_pages/files.html", context)


# About Gallary
def about_gallary(request):
    context = {"page": "About"}
    try:
        context["images"] = models.Image.objects.filter(page="About").order_by('-id')
    except ObjectDoesNotExist:
        pass
    return render(request, "fiid_india_pages/gallary.html", context)


# Programmes Gallary
def programmes_gallary(request):
    context = {"page": "Programmes"}
    try:
        context["images"] = models.Image.objects.filter(page="Programmes").order_by('-id')
    except ObjectDoesNotExist:
        pass
    return render(request, "fiid_india_pages/gallary.html", context)
