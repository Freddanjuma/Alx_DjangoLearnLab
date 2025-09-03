### Retrieve a Book

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book)



#### 2. `update.md`
```bash
cat > update.md << 'EOF'
### Update a Book

**Command:**
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)


#### 3. `delete.md`
```bash
cat > delete.md << 'EOF'
### Delete a Book

**Command:**
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()


#### 4. `CRUD_operations.md`
```bash
cat > CRUD_operations.md << 'EOF'
# CRUD Operations Summary

## Create
```python
Book.objects.create(
    title="1984",
    author="George Orwell",
    published_date=date(1949, 6, 8),
    isbn="9780451524935",
    price=19.84
)

Book.objects.get(title="1984")

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

