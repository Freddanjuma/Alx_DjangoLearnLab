# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # ... your existing paths for books and library ...
    path('books/', list_books, name='all-books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    # Add these new URL patterns for authentication
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]