from django.urls import path

from . import views

app_name = 'lawsuits'
urlpatterns = [
    path('', views.lawsuits, name='lawsuits'),
    path('movement/<int:lawsuit_id>/', views.movement, name='movement'),

]