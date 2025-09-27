from django.db import models

# Create your models here.
# api/models.py


class Author(models.Model):
    """
    Represents an author of books.
    """
    name = models.CharField(max_length=255, unique=True)
    # Add other author-related fields if necessary later, e.g., birth_date, nationality

    class Meta:
        ordering = ['name'] # Orders authors by name by default

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book with a title, publication year, and an author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    # ForeignKey links Book to Author.
    # on_delete=models.CASCADE means if an Author is deleted, all their Books are also deleted.
    # related_name='books' allows you to access books from an Author instance, e.g., author_instance.books.all()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    class Meta:
        # Ensures that an author cannot have two books with the exact same title and publication year
        unique_together = ('title', 'author', 'publication_year')
        ordering = ['title'] # Orders books by title by default

    def __str__(self):
        return f"{self.title} by {self.author.name} ({self.publication_year})"