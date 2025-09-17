# LibraryProject/relationship_app/models.py

# Import necessary modules from Django's database layer and authentication system.
from django.db import models
from django.contrib.auth import get_user_model # Function to retrieve the active user model.

# Get the custom user model defined in settings.AUTH_USER_MODEL.
# Documentation: This ensures all references to 'User' across the application correctly
# point to our custom user model (bookshelf.CustomUser), centralizing user management.
User = get_user_model()

# Import signals for automated tasks (e.g., creating user profiles).
from django.db.models.signals import post_save
from django.dispatch import receiver

# IMPORTANT: Author and Book models are defined in 'bookshelf/models.py'.
# We import 'Book' here because it's used in the 'Library' model's ManyToManyField.
# Do NOT define 'Author' or 'Book' models in this file to avoid duplication and conflicts.
from bookshelf.models import Book # Import Book model from the 'bookshelf' app.

# --- User Profile Model ---
# This model extends the CustomUser model with additional profile information (e.g., role).
# It uses a OneToOneField to link directly to a CustomUser instance, ensuring each user has one profile.
class UserProfile(models.Model):
    # Link to the CustomUser model. CASCADE ensures if a User is deleted, their profile is too.
    # 'related_name' allows accessing the profile from a user instance (e.g., user.profile).
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',
                                help_text="The associated user for this profile.")

    # Define choices for user roles. This limits input and helps with clear role management.
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    # 'role' field to store the user's role, defaulting to 'Member'.
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member',
                            help_text="The role of the user within the library system.")

    # String representation for admin and debugging.
    def __str__(self):
        return f"{self.user.username} - {self.role}"

    # Documentation: UserProfile is part of our authorization system, providing a flexible
    # way to assign and retrieve user roles beyond Django's built-in groups system if needed.
    # Using choices for roles ensures data integrity and prevents invalid role assignments.


# --- Signals to Automate UserProfile Creation and Saving ---

# Signal receiver: Automatically creates a UserProfile when a new User is created.
# This ensures every new user gets an associated profile without manual intervention.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # 'created' is a boolean flag, true if a new instance was just saved.
    if created:
        UserProfile.objects.create(user=instance)
        # Documentation: Signals help maintain data consistency. This prevents
        # 'UserProfile.DoesNotExist' errors when trying to access user.profile.

# Signal receiver: Automatically saves the UserProfile when the associated User is saved.
# This keeps the profile in sync with user updates.
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Check if the instance already has a related UserProfile to avoid errors on first creation
    # (though create_user_profile handles initial creation)
    if hasattr(instance, 'profile'): # Changed from 'userprofile' to 'profile' based on related_name
        instance.profile.save()
        # Documentation: 'hasattr' check ensures this signal doesn't try to save a non-existent
        # profile, especially during initial user creation or if profiles are manually deleted.


# --- Library Model ---
# Represents a physical library branch or location.
class Library(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the library branch.")
    # ManyToManyField to link multiple Books to multiple Libraries.
    # 'related_name' allows accessing books from a library (e.g., library.books.all()).
    books = models.ManyToManyField(Book, related_name='libraries',
                                help_text="The collection of books available in this library.")

    # String representation for admin and debugging.
    def __str__(self):
        return self.name

    # Documentation: ManyToManyField implicitly handles the intermediate table,
    # simplifying relationships between books and libraries.


# --- Librarian Model ---
# Represents a librarian staff member and links them to a specific library.
class Librarian(models.Model):
    # OneToOneField to link to a CustomUser instance.
    # This means each User can be a librarian for at most one library.
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                help_text="The user account associated with this librarian.")
    # OneToOneField to link to a Library instance.
    # This means each Library has one head librarian (or a main point of contact).
    # Removed primary_key=True here. It's better for Librarian to have its own auto-ID,
    # and link to Library normally. If library_id IS the primary key of Librarian,
    # you typically set primary_key=True on the user_id field or let Django autogenerate.
    # For a simple 1:1, a regular OneToOneField is standard.
    library = models.OneToOneField(Library, on_delete=models.CASCADE,
                                   help_text="The library branch this librarian manages.")

    # String representation for admin and debugging.
    def __str__(self):
        return f"Librarian: {self.user.username} ({self.library.name})"

    # Documentation: This model establishes a clear relationship between a user (who is a librarian)
    # and the specific library they are assigned to manage. The OneToOneField ensures unique assignments.


# IMPORTANT: Permissions for Book are typically defined within the Book model's Meta class
# in 'bookshelf/models.py'. Do not define them here unless they are custom permissions
# specifically for models defined within 'relationship_app/models.py'.