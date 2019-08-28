from django.urls import path,include

from . import views

app_name = 'master'
urlpatterns = [
    path('', views.index, name='index'),
    path('addtext/', views.addtext, name='addtext'),
    path('login_master/',views.login_master,name='login_master'),
    path('logout_master/',views.logout_master,name='logout_master'),
]