from django.urls import path
from .views import (
    AuthorListCreateView,
    AuthorRetrieveUpdateDestroyView,
    BookListCreateView,
    BookRetrieveUpdateDestroyView
)

"""
URL patterns for the 'api' application.
Defines endpoints for CRUD operations on Author and Book models.
"""
urlpatterns = [
    # Author URLs
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),

    # Book URLs
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]