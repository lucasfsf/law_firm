from xml.etree.ElementInclude import include
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', include("django.contrib.auth.urls")),
]