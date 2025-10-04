from django.db import models

class Author(models.Model):
    """
    Represents an author of books.
    - name: The full name of the author.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book published by an author.
    - title: The title of the book.
    - publication_year: The year the book was published (integer).
    - author: A foreign key to the Author model, establishing a one-to-many relationship.
              An Author can have multiple Books (related_name='books').
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year}) by {self.author.name}"