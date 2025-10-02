from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters # Import filters for SearchFilter and OrderingFilter

from django.contrib.auth.models import User
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer, UserSerializer # Corrected import for UserSerializer
from .filters import BookFilter # Import the custom BookFilter

# User API Views
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can list users

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can retrieve user details

# Author API Views
class AuthorListCreateView(generics.ListCreateAPIView): # This is the view name
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Authenticated can create, all can list

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Authenticated can update/delete, all can retrieve

# Book API Views
class BookListView(generics.ListAPIView):
    """
    API view to list books with filtering, searching, and ordering capabilities.
    Accessible by all (read-only), but write operations are handled by separate views
    requiring authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Read-only for unauthenticated users

    # Configure filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter # Specify the custom filterset for DjangoFilterBackend
    search_fields = ['title', 'author__name', 'isbn'] # Fields to search across
    ordering_fields = ['title', 'published_date'] # Fields to order by

class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book. Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can create books

class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single book by ID. Accessible by all.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Read-only for unauthenticated users

class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book. Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can update books

class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete an existing book. Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can delete books