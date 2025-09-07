from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Paths for book and library views
    path('books/', views.list_books, name='all-books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),

    # Authentication URLs - FIXED TEMPLATE PATHS
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),  #  custom view
    path('logout/', auth_views.LogoutView.as_view(
        template_name='relationship_app/logout.html',  # FIXED PATH
        next_page='relationship_app:login'
    ), name='logout'),
    path('profile/', views.profile, name='profile'),  
]