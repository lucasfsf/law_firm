from django.urls import path

from . import views

app_name = 'lawsuits'
urlpatterns = [
    path('', views.lawsuits, name='lawsuits')
]