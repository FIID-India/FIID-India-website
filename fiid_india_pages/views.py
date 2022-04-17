from django.conf import settings
from django.shortcuts import render
from . import models
from . import forms
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from . send_email import contact_email, subscriber_welcome_email

def home_page_view(request):
    form = forms.SubscribeForm()
    context = {}
    try:
        about = models.Page.objects.get(name="About")
        context["about"] = about
        context["about_images"] = about.image_set.all().order_by('-id')[:1]
    except ObjectDoesNotExist:
        pass

    try:
        programmes = models.Page.objects.get(name="Programmes")
        context["programmes"] = programmes
        context["programmes_images"] = programmes.image_set.all().order_by('-id')[:1]
    except ObjectDoesNotExist:
        pass

    try:
        objectives = models.Page.objects.get(name="Objectives")
        context["objectives"] = objectives
        context["objectives_images"] = objectives.image_set.all().order_by('-id')[:1]
    except:
        pass

    try:
        carousel = models.Carousel.objects.all().order_by('-id')[:3]
        context["carousel"] = carousel
        
    except:
        pass

    if request.method == "POST":
        form = forms.SubscribeForm(request.POST)
        if form.is_valid():
            full_name = request.POST['full_name']
            recipient = [request.POST['email']]
            form.save()
            form = forms.SubscribeForm()

            subject = f"Welcome "+full_name
            subscriber_welcome_email(full_name, subject, recipient, 'welcome.html')

            message= f"Great "+full_name+"!! Your are added to our subscribers list"
            messages.success(request, message)
        else:
            for field, errors in form.errors.items():
                error = '{}'.format(''.join(errors))
                messages.error(request, error)
            
            
    context["form"] = form
    return render(request, "fiid_india_pages/home.html", context)

def about_page_view(request):
    context={}
    try:
        about = models.Page.objects.get(name="About")
        context["about"] = about
        context["about_images"] = about.image_set.all().order_by('-id')[:3]
    except ObjectDoesNotExist:
        pass
    return render(request, "fiid_india_pages/about.html", context)

def programmes_page_view(request):
    context={}
    try:
        programmes = models.Page.objects.get(name="Programmes")
        context["programmes"] = programmes
        context["programmes_images"] = programmes.image_set.all().order_by('-id')[:3]
    except ObjectDoesNotExist:
        pass
    return render(request, "fiid_india_pages/programmes.html", context)

def objectives_page_view(request):
    context={}
    try:
        objectives = models.Page.objects.get(name="Objectives")
        context["objectives"] = objectives
        context["objectives_images"] = objectives.image_set.all().order_by('-id')[:3]
    except ObjectDoesNotExist:
        pass
    return render(request, "fiid_india_pages/objectives.html", context)

def contact_page_view(request):
    form = forms.ContactForm()
    context={}
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
            contact_email(full_name, message_send, recipients, email, subject, 'contact_recive.html')

            message= "Thankyou for contacting us!! We will get back to you soon"
            messages.success(request, message)
        else:
            for field, errors in form.errors.items():
                error = '{}'.format(''.join(errors))
                messages.error(request, error)        
            
    context["form"] = form
    return render(request, "fiid_india_pages/contact.html", context)

def file_page_view(request):
    context={}
    files = models.File.objects.all().order_by('-id')
    context["files"] = files
    return render(request, "fiid_india_pages/files.html", context)

def about_gallary(request):
    context = {"page":"About"}
    try:
        about = models.Page.objects.get(name="About")
        context["images"] = about.image_set.all().order_by('-id')
    except ObjectDoesNotExist:
        pass
    return render(request, "fiid_india_pages/gallary.html", context)

def programmes_gallary(request):
    context = {"page":"Programmes"}
    try:
        about = models.Page.objects.get(name="Programmes")
        context["images"] = about.image_set.all().order_by('-id')
    except ObjectDoesNotExist:
        pass
    return render(request, "fiid_india_pages/gallary.html", context)
