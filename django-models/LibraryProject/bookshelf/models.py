from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    @property
    def publication_year(self):
        return self.published_date.year

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_edit_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"
