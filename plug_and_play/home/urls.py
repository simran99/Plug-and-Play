from django.urls import path,include

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]