# Imports for bookshelf-specific models
from django.db import models
from django.conf import settings 

# --- Bookshelf-specific models go here ---
class Author(models.Model):
    name = models.CharField(max_length=100)
    # Example: created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Example: owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.title