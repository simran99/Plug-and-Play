from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'connect'
urlpatterns = [
    path('', views.index, name='index'),
    # path('accounts/', include('allauth.urls')),
    path('login/',views.login , name='login'),
    path('dashboard/',views.dashboard , name='dashboard'),
    path('logout/',views.logout_view , name='logout'),
    path('showtext/',views.showtext , name='showtext'),
    path('openfile/',views.openfile , name='openfile'),
    path('download/',views.download , name='download'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)