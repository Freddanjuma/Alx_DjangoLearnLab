from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .filters import AuthorFilter, BookFilter # Import your filters

# --- Author Views ---
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AuthorFilter # Use the custom filterset

class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    # Optional: Custom deletion response
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Author deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

# --- Book Views ---
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter # Use the custom filterset

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Optional: Custom deletion response
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Book deleted successfully."}, status=status.HTTP_204_NO_CONTENT)