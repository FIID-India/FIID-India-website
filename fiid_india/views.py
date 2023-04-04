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

    def get_success_url(self):
        return reverse_lazy('fiid-india:contact')
