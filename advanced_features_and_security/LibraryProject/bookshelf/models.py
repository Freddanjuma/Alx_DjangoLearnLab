# LibraryProject/bookshelf/models.py

# Import necessary modules from Django's database layer
from django.db import models
# Import AbstractUser for creating a custom user model that extends Django's base user functionality.
from django.contrib.auth.models import AbstractUser

# --- Custom User Model ---
# This model extends Django's default AbstractUser to add custom fields.
# It is specified as AUTH_USER_MODEL in settings.py, making it the primary user model.
# Documentation: Inheriting from AbstractUser provides all standard user fields (username, password, email, etc.)
# and built-in authentication methods, while allowing custom fields like date_of_birth and profile_photo.
# Security Note: Django's AbstractUser includes robust password hashing and other security features by default.
class CustomUser(AbstractUser):
    # User's date of birth, optional (can be blank in forms and NULL in DB).
    date_of_birth = models.DateField(null=True, blank=True, help_text="Optional: User's date of birth.")
    # User's profile photo, optional, uploaded to 'profile_photos/' directory.
    # Documentation: ImageField handles file uploads; ensure MEDIA_ROOT and MEDIA_URL are configured in settings.py.
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True, help_text="Optional: User's profile photo.")

    # Override default many-to-many fields for groups and user permissions.
    # This is necessary when using a custom user model to prevent reverse accessor clashes
    # with Django's built-in auth app's default 'User' model (even though we're replacing it).
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set', # Unique related_name for reverse lookups
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set', # Unique related_name for reverse lookups
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )
    # Documentation: Custom related_names are critical when defining a custom user model
    # to avoid conflicts with Django's default 'User' model reverse relations.

    # String representation for admin and debugging.
    def __str__(self):
        return self.username

# --- Author Model ---
# Represents an author of books in the library.
class Author(models.Model):
    name = models.CharField(max_length=100, help_text="The full name of the author.")
    bio = models.TextField(blank=True, null=True, help_text="Optional: A short biography of the author.")

    # String representation of an Author object, useful for admin and debugging.
    def __str__(self):
        return self.name

    # Documentation: Django models handle database interactions securely (ORM),
    # preventing SQL injection. Fields like CharField and TextField also provide
    # implicit protection against certain injection attacks by sanitizing input.

# --- Book Model ---
# Represents a book available in the library.
class Book(models.Model):
    title = models.CharField(max_length=200, help_text="The title of the book.")
    # ForeignKey to Author model: A book has one author, an author can have many books.
    # on_delete=models.CASCADE means if an Author is deleted, all their books are also deleted.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, help_text="The author of the book.")
    published_date = models.DateField(help_text="The date the book was first published.")
    isbn = models.CharField(max_length=13, unique=True, help_text="The International Standard Book Number (13 digits), must be unique.")

    # --- NEW FIELD ADDED HERE: GENRE ---
    # CharField for storing the book's genre. It's optional (blank=True, null=True).
    genre = models.CharField(max_length=50, blank=True, null=True,
                             help_text="Optional: The genre or category of the book (e.g., Fiction, Sci-Fi, Fantasy).")
    # Documentation: Adding 'blank=True' allows the field to be empty in forms,
    # and 'null=True' allows it to be NULL in the database, making it optional.
    # This is important when adding new fields to existing models, as old records
    # won't have this data.


    # String representation of a Book object.
    def __str__(self):
        return f"{self.title} by {self.author.name}"