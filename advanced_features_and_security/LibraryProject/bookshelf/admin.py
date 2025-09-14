from django.contrib import admin
from .models import Author, Book # Import your bookshelf models

admin.site.register(Author)
admin.site.register(Book)