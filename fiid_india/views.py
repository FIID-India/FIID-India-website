from django.views import generic

class HomePageView(generic.TemplateView):
    template_name = 'fiid_india/home.html'
