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

