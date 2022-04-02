from django.urls import path
from . import views

app_name = 'fiid-india-pages'

urlpatterns = [
    path('', views.home_page_view, name="home-page"),
    path('about/', views.about_page_view, name="about-page"),
]