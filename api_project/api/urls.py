# api_project/api/urls.py

from django.urls import path, include # Ensure 'include' is here
from rest_framework.routers import DefaultRouter 
from .views import BookList, BookViewSet 

# Create a router instance
router = DefaultRouter() # Arouter that can generate standard RESTful URLs

# Register your ViewSet with the router
# r'books_all' is the URL prefix for this ViewSet
# BookViewSet is the ViewSet class
# basename='book_all' is used for reverse lookup of URLs
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView) - KEEP THIS AS PER INSTRUCTIONS
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]