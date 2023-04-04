from django.urls import path
from .import views

app_name = 'fiid-india'


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('programs/', views.ProgramsPageView.as_view(), name='programmes'),
    path('objectives/', views.ObjectivesPageView.as_view(), name='objectives'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
]
