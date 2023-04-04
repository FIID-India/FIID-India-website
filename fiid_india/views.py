from django.views import generic

class HomePageView(generic.TemplateView):
    template_name = 'fiid_india/home.html'


class AboutPageView(generic.TemplateView):
    template_name = 'fiid_india/about.html'
    
    
class ProgramsPageView(generic.TemplateView):
    template_name = 'fiid_india/programmes.html'


class ObjectivesPageView(generic.TemplateView):
    template_name = 'fiid_india/objectives.html'