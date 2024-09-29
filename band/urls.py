from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('register/', register, name='register'),
    path('create_event/', views.create_event, name='create_event'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
