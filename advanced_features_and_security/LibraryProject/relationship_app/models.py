# relationship_app/models.py - CLEAN AND CONSOLIDATED CONTENT

from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model() # This now correctly refers to bookshelf.CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# IMPORTANT: Author and Book models are in bookshelf/models.py.
# Do NOT define them here. If you need to reference them, use 'bookshelf.Book' etc.
from bookshelf.models import Book # Import Book for the ManyToManyField below

# UserProfile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'), # FIX: Removed an extra parenthesis here
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Signals to create/save UserProfile automatically
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Ensure profile exists before saving
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()

# Library Model
class Library(models.Model):
    name = models.CharField(max_length=100)
    # Reference Book from the 'bookshelf' app
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

# Librarian Model
class Librarian(models.Model):
    # User field for the librarian (can be a CustomUser)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Link to the Library
    library = models.OneToOneField(Library, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Librarian: {self.user.username} ({self.library.name})"

# Ensure permissions for Book are defined ONLY in bookshelf/models.py, not here.
# If you need custom permissions for models defined *here*, define them within their Meta class.