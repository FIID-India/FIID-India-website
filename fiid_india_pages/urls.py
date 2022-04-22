from django.urls import path
from . import views

app_name = 'fiid-india-pages'

urlpatterns = [
    path('', views.home_page_view, name="home-page"),
    path('about/', views.about_page_view, name="about-page"),
    path('about/gallary/', views.about_gallary, name="about-gallary"),
    path('programmes/', views.programmes_page_view, name="programmes-page"),
    path('programmes/gallary/', views.programmes_gallary,
         name="programmes-gallary"),
    path('objectives/', views.objectives_page_view, name="objectives-page"),
    path('contact/', views.contact_page_view, name="contact-page"),
    path('files/', views.file_page_view, name="files-page"),
]
