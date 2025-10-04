# django_blog/blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('posts/', views.post_list_view, name='posts'),
    path('login/', views.login_view, name='login'),      # Add this line
    path('register/', views.register_view, name='register'), # Add this line
]