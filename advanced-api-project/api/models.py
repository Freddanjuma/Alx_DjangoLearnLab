from django.db import models

class Author(models.Model):
    """
    Represents an author with a name and an optional biography.
    The 'name' field is unique to prevent duplicate authors.
    """
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        """Returns the string representation of the Author."""
        return self.name

class Book(models.Model):
    """
    Represents a book with a title, ISBN, author, and published date.
    Each book must be linked to an existing Author.
    """
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField(blank=True, null=True)

    def __str__(self):
        """Returns the string representation of the Book."""
        return f"{self.title} by {self.author.name}"

    class Meta:
        """Metadata options for the Book model."""
        ordering = ['title'] # Default ordering for books