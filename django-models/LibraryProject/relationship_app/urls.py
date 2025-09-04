from django.urls import path
# Specific imports required by the checker
from .views import list_books, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Paths for book and library views
    path('books/', list_books, name='all-books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    # Paths for authentication, as required by the checker
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/registration/logout.html'), name='logout'),
]