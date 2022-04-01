from django.urls import path
from . import views

app_name = 'fiid-india-pages'

urlpatterns = [
    path('', views.home_page_view, name="home-page"),
]