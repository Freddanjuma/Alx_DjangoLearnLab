# relationship_app/urls.py
from django.urls import path
# CORRECTED import for the checker
from .views import list_books, LibraryDetailView

urlpatterns = [
    # URL for the function-based view of all books
    path('books/', list_books, name='all-books'),
    
    # URL for the class-based view of a specific library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]