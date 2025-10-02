from django.urls import path
from .views import (
    UserList, UserDetail,
    AuthorListCreateView, AuthorDetailView, # CORRECTED: Changed AuthorListView to AuthorListCreateView
    BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView
)

urlpatterns = [
    # User URLs
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    # Author URLs
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'), # CORRECTED: Used AuthorListCreateView
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    # Book URLs
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]