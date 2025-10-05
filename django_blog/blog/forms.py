# django_blog/blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    last_name = forms.CharField(max_length=150, required=False, help_text="Optional.")

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name',)
        # 'username' is included by default from UserCreationForm.Meta.fields

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name',)


 #Explanation:

# CustomUserCreationForm extends Django's default UserCreationForm to explicitly add email as a required field.
# We also add first_name and last_name to the registration form, as these are common profile details.
# CustomUserChangeForm is included here as a placeholder for when we later implement the profile editing view; it's a good practice to define it now.