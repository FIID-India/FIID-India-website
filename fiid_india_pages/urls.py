from django.urls import path
from . import views

app_name = 'fiid-india-pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home-page"),
    path('about/', views.AboutPageView.as_view(), name="about-page"),
    path('programmes/', views.ProgrammesPageView.as_view(), name="programmes-page"),
    path('gallary/', views.GallaryPageView.as_view(), name="gallary-page"),
    path('objectives/', views.ObjectivesPageView.as_view(), name="objectives-page"),
    path('contact/', views.contact_page_view, name="contact-page"),
    path('files/', views.FilesPageView.as_view(), name="files-page"),
]
