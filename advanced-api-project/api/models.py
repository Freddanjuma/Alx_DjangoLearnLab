from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"
