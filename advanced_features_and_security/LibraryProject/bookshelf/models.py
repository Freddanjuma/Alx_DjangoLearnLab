# bookshelf/models.py (Contains CustomUser, Author, Book)
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone # For CustomUserManager

# --- CustomUserManager definition (FULLY HERE NOW) ---
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, email, password, **extra_fields)

# --- CustomUser model definition (FULLY HERE NOW) ---
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    objects = CustomUserManager()
    def __str__(self):
        return self.username

# --- Author model (already here) ---
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# --- Book model (already here with correct fields) ---
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField(blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True, unique=True)
    def __str__(self):
        return self.title