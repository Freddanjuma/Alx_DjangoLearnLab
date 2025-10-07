from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home page (fixes the 'home' reverse issue)
    path('', views.post_list_view, name='home'),  # 👈 Add this name
    path('posts/', views.post_list_view, name='post_list'),

    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
