from django.contrib import admin

# Register your models here.
# api/admin.py

from .models import Author, Book

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)