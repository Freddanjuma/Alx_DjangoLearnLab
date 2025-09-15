# bookshelf/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Book, Author # Import CustomUser and other models from bookshelf

# Form for CustomUser creation
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta): # Inherit Meta from UserCreationForm
        model = CustomUser
        # Ensure 'date_of_birth' and 'profile_photo' are included
        fields = UserCreationForm.Meta.fields + ('date_of_birth', 'profile_photo',)

# Form for CustomUser changing (optional, but good practice)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields # Include all fields you want to allow changing

# Form for Book model
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date", "isbn"] # Ensure these fields match your Book model

# Form for Author model (optional)
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

        # bookshelf/forms.py

# (Your existing imports and other form definitions would be here)

from django import forms # Ensure this is at the top if not already there
from .models import Book # Ensure Book model is imported

# Add the BookForm class here, typically at the bottom or logically grouped
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']
        # You can customize widgets here later if needed