# django_blog/blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm

# --- ENSURE THIS FUNCTION IS HERE AND CORRECT ---
def home_view(request):
    return render(request, 'blog/base.html', {})
# ------------------------------------------------

def post_list_view(request):
    return render(request, 'blog/post_list.html', {})

def register_view(request):
    # ... (your register_view code) ...
    pass # Placeholder

@login_required
def profile_view(request):
    # ... (your profile_view code) ...
    pass # Placeholder