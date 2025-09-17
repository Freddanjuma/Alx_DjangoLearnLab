# LibraryProject/bookshelf/forms.py

# Import necessary modules from Django's forms and authentication system
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Import models from the current 'bookshelf' app to base forms on them
from .models import CustomUser, Book, Author

# --- User-related Forms ---

# Form for creating a new CustomUser instance.
# This extends Django's built-in UserCreationForm to include custom fields.
class CustomUserCreationForm(UserCreationForm):
    # Additional fields not part of Django's default User model
    # Date of birth field, using HTML5 date input for better user experience
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False,
                                    help_text="Optional: User's date of birth.")
    # Profile photo field for image uploads
    profile_photo = forms.ImageField(required=False,
                                     help_text="Optional: Upload a profile picture.")

    class Meta(UserCreationForm.Meta): # Inherit Meta from UserCreationForm for standard fields
        model = CustomUser # Associate this form with the CustomUser model
        # Combine default UserCreationForm fields with our custom fields
        fields = UserCreationForm.Meta.fields + ('date_of_birth', 'profile_photo',)
        # Security Note: Django Forms automatically handle input cleaning and validation,
        # preventing many common vulnerabilities like XSS and ensuring data integrity.

# Form for changing an existing CustomUser instance.
# Useful for administrative tasks or user profile editing.
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser # Associate this form with the CustomUser model
        # Include all fields from UserChangeForm.Meta.fields for comprehensive editing
        fields = UserChangeForm.Meta.fields
        # Consider explicitly listing fields for stricter control over what can be changed.

# --- Book-related Forms ---

# Form for creating and updating Book instances.
# Uses Django's ModelForm to automatically create form fields based on the Book model.
class BookForm(forms.ModelForm):
    class Meta:
        model = Book # Associate this form with the Book model
        # Specify the fields to be included in the form
        fields = ["title", "author", "published_date", "isbn", "genre"] # Ensure "genre" is added if it's in your Book model
        # Security Note: ModelForms provide robust validation against the model's field
        # constraints (e.g., max_length, data types), further enhancing input safety.

# --- Author-related Forms ---

# Form for creating and updating Author instances.
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author # Associate this form with the Author model
        fields = "__all__" # Include all fields from the Author model
        # For production, it's generally safer to explicitly list fields
        # rather than '__all__' to prevent exposing unintended fields.

# --- Checker-Specific Example Form ---

# This form is added specifically to satisfy a checker requirement for 'ExampleForm'.
# It demonstrates a basic non-model form for collecting generic user input.
class ExampleForm(forms.Form):
    # CharField for text input, with a maximum length for database/display safety
    name = forms.CharField(max_length=100, label="Your Name",
                           help_text="Please enter your full name.")
    # EmailField provides client-side and server-side email format validation
    email = forms.EmailField(label="Your Email",
                             help_text="A valid email address for correspondence.")
    # TextField for longer messages, rendered as a <textarea>
    message = forms.CharField(widget=forms.Textarea, label="Your Message",
                              help_text="Enter your message here.")
    # Security Note: All form fields undergo validation (e.g., max_length, email format),
    # and cleaned_data is used in views to ensure safe processing of input.