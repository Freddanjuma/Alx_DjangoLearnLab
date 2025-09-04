# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL for the function-based view of all books
    path('books/', views.all_books, name='all-books'),

    # URL for the class-based view of a specific library
    # The <int:pk> part captures the library's ID from the URL
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
]