from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_pic']

class EditProfileForm(UserChangeForm):
    password = None  # hide password field
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_pic']
