# django_blog/blog/urls.py
from django.urls import path
from . import views # Import views from the current app
from django.contrib.auth import views as auth_views # Import Django's built-in auth views

urlpatterns = [
    # Blog Core Views
    path('', views.home_view, name='home'),
    path('posts/', views.post_list_view, name='post_list'), 

    # Authentication URLs
    path('register/', views.register_view, name='register'), # Custom registration view
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'), 
    path('profile/', views.profile_view, name='profile'), # Custom profile view
]