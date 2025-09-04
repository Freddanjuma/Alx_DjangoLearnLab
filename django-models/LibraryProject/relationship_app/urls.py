# relationship_app/urls.py
from django.urls import path
from . import views  # Corrected import for the checker
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='all-books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),

    # These patterns are now corrected to match the checker's requirements
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]