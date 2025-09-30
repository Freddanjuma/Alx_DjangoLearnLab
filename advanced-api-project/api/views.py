from rest_framework import generics, permissions, status # Ensure 'status' is imported
from rest_framework.response import Response # Ensure 'Response' is imported
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .filters import AuthorFilter, BookFilter

# --- Author Views ---
class AuthorListView(generics.ListAPIView):
    """
    API endpoint that allows for listing all Authors.
    Unauthenticated users have read-only access.
    Supports filtering.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AuthorFilter

class AuthorDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows for retrieving a single Author by ID.
    Unauthenticated users have read-only access.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuthorCreateView(generics.CreateAPIView):
    """
    API endpoint that allows for creating a new Author.
    Requires authentication.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can create

class AuthorUpdateView(generics.UpdateAPIView):
    """
    API endpoint that allows for updating an existing Author.
    Requires authentication.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can update

class AuthorDeleteView(generics.DestroyAPIView):
    """
    API endpoint that allows for deleting an existing Author.
    Requires authentication.
    Returns a custom success message upon deletion.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer # Serializer is technically optional for Destroy, but good practice
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can delete

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Author deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# --- Book Views ---
class BookListView(generics.ListAPIView):
    """
    API endpoint that allows for listing all Books.
    Unauthenticated users have read-only access.
    Supports filtering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter

class BookDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows for retrieving a single Book by ID.
    Unauthenticated users have read-only access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    API endpoint that allows for creating a new Book.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can create

class BookUpdateView(generics.UpdateAPIView):
    """
    API endpoint that allows for updating an existing Book.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can update

class BookDeleteView(generics.DestroyAPIView):
    """
    API endpoint that allows for deleting an existing Book.
    Requires authentication.
    Returns a custom success message upon deletion.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer # Serializer is technically optional for Destroy, but good practice
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can delete

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Book deleted successfully."}, status=status.HTTP_204_NO_CONTENT)