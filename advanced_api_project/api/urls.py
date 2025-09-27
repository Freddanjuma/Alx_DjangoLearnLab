# advanced_api_project/api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# Example: If you were creating simple API views
# from .views import AuthorList, AuthorDetail, BookList, BookDetail

urlpatterns = [
    # path('authors/', AuthorList.as_view(), name='author-list'),
    # path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    # path('books/', BookList.as_view(), name='book-list'),
    # path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]

# This is often used with DRF to allow content negotiation via URL suffix (e.g., .json, .api)
urlpatterns = format_suffix_patterns(urlpatterns)