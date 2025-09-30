from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Handles conversion of Book model instances to JSON and vice-versa.
    Includes custom validation for specific fields and object-level checks.
    """
    # Read-only field to display the author's name instead of just the ID
    author_name = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'author', 'author_name', 'published_date']
        read_only_fields = ['id', 'author_name'] # 'id' is generated, 'author_name' is derived

    def validate_title(self, value):
        """
        Custom validation for the 'title' field.
        Ensures that the book title does not consist only of numeric characters.
        """
        if value and value.isdigit():
            raise serializers.ValidationError("Book title cannot consist only of numbers.")
        return value

    def validate_isbn(self, value):
        """
        Custom validation for the 'isbn' field.
        Ensures ISBN is exactly 13 characters long if provided.
        """
        if value and len(value) != 13:
            raise serializers.ValidationError("ISBN must be 13 characters long.")
        return value

    def validate(self, data):
        """
        Object-level validation for the BookSerializer.
        Ensures that a book with the same title by the same author does not already exist.
        This prevents duplicate entries for a specific author's work.
        """
        title = data.get('title')
        author = data.get('author')

        if title and author:
            qs = Book.objects.filter(title=title, author=author)
            # Exclude the current instance itself during update operations
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError(
                    "A book with this title already exists for this author."
                )
        return data

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Handles conversion of Author model instances to JSON and vice-versa.
    Includes custom validation for the 'name' field.
    """
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']
        read_only_fields = ['id']

    def validate_name(self, value):
        """
        Custom validation for the 'name' field.
        Ensures the author's name is at least 3 characters long.
        """
        if len(value) < 3:
            raise serializers.ValidationError("Author name must be at least 3 characters long.")
        return value