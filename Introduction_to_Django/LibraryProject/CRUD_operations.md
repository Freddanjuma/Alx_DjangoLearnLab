# CRUD Operations Summary

## Create
```python
from bookshelf.models import Book
from datetime import date

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    published_date=date(1949, 6, 8),
    isbn="9780451524935",
    price=19.84
)
print(book)
# <Book: 1984 by George Orwell>

# Get all books
books = Book.objects.all()
print(books)

# Get a specific book by ID
book = Book.objects.get(id=1)
print(book)

# Filter books by author
orwell_books = Book.objects.filter(author="George Orwell")
print(orwell_books)

book = Book.objects.get(id=1)
book.price = 25.00
book.save()
print(book.price)  # 25.00

book = Book.objects.get(id=1)
book.delete()
print(Book.objects.all())

