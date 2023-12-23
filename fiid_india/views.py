from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from . models import Message


class HomePageView(generic.TemplateView):
    template_name = 'fiid_india/home.html'


class AboutPageView(generic.TemplateView):
    template_name = 'fiid_india/about.html'


class ProgramsPageView(generic.TemplateView):
    template_name = 'fiid_india/programmes.html'


class ObjectivesPageView(generic.TemplateView):
    template_name = 'fiid_india/objectives.html'


class ContactPageView(generic.CreateView):
    model = Message
    template_name = 'fiid_india/contact.html'
    fields = '__all__'
    
    def form_valid(self, form):
        notification = "The message has been sent successfully"
        messages.success(self.request, notification)
        return super(ContactPageView, self).form_valid(form)
    
    def form_invalid(self, form):
        notification = "Couldn't send the message. Please try later"
        messages.error(self.request, notification)
        return super(ContactPageView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('fiid-india:contact')
