from django.shortcuts import render
from . import models
from . import forms
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


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
            form.save()
            form = forms.SubscribeForm()
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
