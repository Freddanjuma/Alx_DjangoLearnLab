# bookshelf/admin.py

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    
    # CORRECTED LINE: Remove 'publication_year' from this list
    list_filter = ('author',)
    
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)