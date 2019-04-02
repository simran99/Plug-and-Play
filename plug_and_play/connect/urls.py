from django.urls import path,include

from . import views

app_name = 'connect'
urlpatterns = [
    path('', views.index, name='index'),
    # path('accounts/', include('allauth.urls')),
    path('login/',views.login , name='login'),
    path('dashboard/',views.dashboard , name='dashboard'),
    path('logout/',views.logout_view , name='logout'),
]