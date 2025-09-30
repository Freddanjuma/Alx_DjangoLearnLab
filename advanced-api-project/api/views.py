from rest_framework import generics, permissions # Ensure 'permissions' is imported
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .filters import AuthorFilter, BookFilter

# --- Author Views ---
class AuthorListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows for listing all Authors or creating a new Author.

    - GET /api/authors/: Retrieves a list of all authors.
      - Supports filtering (e.g., ?name__icontains=john).
      - Unauthenticated users have read-only access (can list authors).
    - POST /api/authors/: Creates a new author.
      - Requires authentication. Only authenticated users can create authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Restricts creation to authenticated users
    filter_backends = [DjangoFilterBackend] # Enables filtering
    filterset_class = AuthorFilter # Specifies the filterset to use

class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows for retrieving, updating, or deleting a single Author.

    - GET /api/authors/<int:pk>/: Retrieves details of a specific author.
      - Unauthenticated users have read-only access.
    - PUT /api/authors/<int:pk>/: Fully updates an existing author.
      - Requires authentication.
    - PATCH /api/authors/<int:pk>/: Partially updates an existing author.
      - Requires authentication.
    - DELETE /api/authors/<int:pk>/: Deletes an existing author.
      - Requires authentication.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Restricts update/delete to authenticated users

    def destroy(self, request, *args, **kwargs):
        """
        Customizes the response message upon successful deletion of an Author.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Author deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# --- Book Views ---
class BookListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows for listing all Books or creating a new Book.

    - GET /api/books/: Retrieves a list of all books.
      - Supports filtering (e.g., ?title__icontains=python, ?author=1, ?published_after=2023-01-01).
      - Unauthenticated users have read-only access (can list books).
    - POST /api/books/: Creates a new book.
      - Requires authentication. Only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Restricts creation to authenticated users
    filter_backends = [DjangoFilterBackend] # Enables filtering
    filterset_class = BookFilter # Specifies the filterset to use

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows for retrieving, updating, or deleting a single Book.

    - GET /api/books/<int:pk>/: Retrieves details of a specific book.
      - Unauthenticated users have read-only access.
    - PUT /api/books/<int:pk>/: Fully updates an existing book.
      - Requires authentication.
    - PATCH /api/books/<int:pk>/: Partially updates an existing book.
      - Requires authentication.
    - DELETE /api/books/<int:pk>/: Deletes an existing book.
      - Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Restricts update/delete to authenticated users

    def destroy(self, request, *args, **kwargs):
        """
        Customizes the response message upon successful deletion of a Book.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Book deleted successfully."}, status=status.HTTP_204_NO_CONTENT)