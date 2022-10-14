from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', include("django.contrib.auth.urls")),
    path('password-change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('articles:index')), name='password_change'),
]