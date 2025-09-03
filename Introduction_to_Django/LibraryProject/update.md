### Update a Book

**Command:**
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)


#### 2. `delete.md`
```bash
cat > delete.md << 'EOF'
### Delete a Book

**Command:**
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

