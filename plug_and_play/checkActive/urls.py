from django.urls import path,include

from . import views

app_name = 'checkActive'
urlpatterns = [
    path('', views.index, name='index'),
]