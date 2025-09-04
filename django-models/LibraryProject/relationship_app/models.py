from django.db import models

# One author can write many books.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# A book has one author. This is a Many-to-One relationship.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

# A library can have many books, and a book can be in many libraries.
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

# Each library has exactly one librarian.
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name