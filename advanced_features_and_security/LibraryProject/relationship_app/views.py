# relationship_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm # Keep this standard form
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, permission_required

# --- Import forms for CustomUser from bookshelf app (where CustomUser now lives) ---
# If you created CustomUserCreationForm in bookshelf/forms.py
from bookshelf.forms import CustomUserCreationForm # <-- CHANGED IMPORT PATH

# --- Import models from bookshelf ---
from bookshelf.models import Book # Keep this import, it's correct now
from .forms import BookForm # This is BookForm defined in relationship_app/forms.py

# Registration view
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) # Use CustomUserCreationForm
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after registration
            messages.success(request, "Registration successful.")
            return redirect("relationship_app:login")
    else:
        form = CustomUserCreationForm() # Use CustomUserCreationForm
    return render(request, "relationship_app/register.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("relationship_app:profile")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# Logout view
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return render(request, "relationship_app/logout.html")

# Simple profile view
def profile_view(request):
    return render(request, "relationship_app/profile.html")

# Helper functions for role checking
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

@permission_required("bookshelf.add_book") # Correct permission name format for Book model in 'bookshelf'
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("relationship_app:book_list") # Assuming you have a book_list URL name
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})

@permission_required("bookshelf.change_book") # Correct permission name format
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("relationship_app:book_list") # Assuming you have a book_list URL name
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/edit_book.html", {"form": form})

@permission_required("bookshelf.delete_book") # Correct permission name format
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("relationship_app:book_list") # Assuming you have a book_list URL name
    return render(request, "relationship_app/delete_book.html", {"book": book})