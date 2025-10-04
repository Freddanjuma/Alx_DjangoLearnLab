from rest_framework import serializers
from .models import Author, Book
from datetime import date # For custom validation

# --- Book Serializer (for individual books) ---
class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Serializes all fields of the Book model.
    Includes custom validation to ensure 'publication_year' is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__' # Serializes 'id', 'title', 'publication_year', 'author'

    def validate_publication_year(self, value):
        """
        Custom validation for 'publication_year'.
        Ensures the publication year is not in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# --- Author Serializer (with nested books) ---
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    - name: The author's name.
    - books: A nested serializer field that represents all books associated with this author.
             It uses BookSerializer to serialize each related book dynamically.
             This demonstrates a one-to-many relationship being represented as a nested list.
    """
    # Nested serializer for the 'books' related_name from the Author model
    # many=True because an author can have many books.
    # read_only=True means these nested books cannot be created/updated directly
    # when creating/updating an Author; they are just displayed.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books'] # Include 'books' for nesting

# --- How the relationship between Author and Book is handled in serializers ---
"""
In AuthorSerializer:
- The 'books' field is defined as `BookSerializer(many=True, read_only=True)`.
- `many=True` indicates that an Author can have multiple books, and each will be serialized.
- `read_only=True` ensures that when you create or update an Author, you cannot simultaneously
  create or update their associated books directly through the AuthorSerializer payload.
  The nested books are purely for representation (reading) purposes in this setup.
- This creates a nested structure where an Author's details include a list of their books,
  making the API response more informative for clients.

In BookSerializer:
- It's a standard ModelSerializer for the Book model.
- The 'author' field (a ForeignKey) will by default be represented as its primary key (ID)
  when BookSerializer is used independently (e.g., when creating a book).
- When BookSerializer is *nested* within AuthorSerializer, it serializes the entire Book object
  for display.
"""