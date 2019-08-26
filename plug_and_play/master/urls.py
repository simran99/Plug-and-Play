from django.urls import path,include

from . import views

app_name = 'master'
urlpatterns = [
    path('', views.index, name='index'),
    path('addtext/', views.addtext, name='addtext'),
]