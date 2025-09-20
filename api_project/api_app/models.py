# APIProject/api_app/models.py
from django.db import models

# Model: Book
# This model represents a book with a title and an author.
# It's designed to be simple for demonstration in an API.
class Book(models.Model):
    # CharField for the book's title. Max length is required for database columns.
    # This field cannot be blank and must be unique (no two books with the exact same title).
    title = models.CharField(max_length=200, unique=True, null=False, blank=False)

    # CharField for the author's name. Max length is required.
    # This field cannot be blank.
    author = models.CharField(max_length=100, null=False, blank=False)

    # A human-readable representation of the Book object.
    # This is useful in the Django admin and for debugging.
    def __str__(self):
        return f"{self.title} by {self.author}"

    # Meta class provides additional options for the model.
    # Here, we order books alphabetically by title by default.
    class Meta:
        ordering = ['title']
        verbose_name = "Book" # Singular name for the model
        verbose_name_plural = "Books" # Plural name for the model