# django_blog/blog/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # Import Django's built-in auth views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('posts/', views.post_list_view, name='posts'),

    # Django's built-in LoginView and LogoutView (using our templates)
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'),

    # Custom Registration View
    path('register/', views.register_view, name='register'),

    # Profile View
    path('profile/', views.profile_view, name='profile'),
]