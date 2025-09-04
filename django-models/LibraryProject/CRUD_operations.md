7 objects imported automatically (use -v 2 for details).

>>> >>> >>> >>> --- 1. CREATE Operation ---
>>> >>> Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> >>> >>> 

>>> >>> >>> --- 2. RETRIEVE Operation ---
>>> >>> my_book = Book.objects.get(title='1984')
>>> >>> >>> print(f'Title: {my_book.title}, Author: {my_book.author}, Year: {my_book.publication_year}')
>>> >>> 

>>> >>> >>> --- 3. UPDATE Operation ---
>>> >>> book_to_update = Book.objects.get(title='1984')
>>> >>> >>> book_to_update.title = 'Nineteen Eighty-Four'
>>> >>> >>> book_to_update.save()
>>> >>> >>> updated_book = Book.objects.get(publication_year=1949)
>>> >>> >>> print(f'Updated Title: {updated_book.title}')
>>> >>> 

>>> >>> >>> --- 4. DELETE Operation ---
>>> >>> book_to_delete = Book.objects.get(title='Nineteen Eighty-Four')
>>> >>> >>> result = book_to_delete.delete()
>>> >>> >>> >>> Book.objects.all()
>>> >>> <QuerySet []>
>>> >>> 