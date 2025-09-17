# relationship_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, permission_required, login_required

# --- Import forms for CustomUser from bookshelf app (where CustomUser now lives) ---
from bookshelf.forms import CustomUserCreationForm

# --- Import models and forms related to Books from bookshelf app ---
# These two lines MUST BE UNCOMMENTED and present:
from bookshelf.models import Book
from bookshelf.forms import BookForm

# --- Authentication Views ---

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            if user.is_superuser or user.is_staff:
                return redirect('relationship_app:admin_view')
            elif user.groups.filter(name='Librarians').exists():
                return redirect('relationship_app:librarian_view')
            elif user.groups.filter(name='Members').exists():
                return redirect('relationship_app:member_view')
            else:
                return redirect('relationship_app:profile')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user.username}!')
            return redirect('relationship_app:login')
        else: # If form is not valid, the errors will be attached to the form and displayed in the template
            pass # The template will display form.errors
    else:
        form = CustomUserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('relationship_app:login')

# --- Profile View ---
@login_required
def profile_view(request):
    return render(request, 'relationship_app/profile_view.html', {})

# --- Role-based Views ---

@user_passes_test(lambda u: u.is_superuser)
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {})

@user_passes_test(lambda u: u.groups.filter(name='Librarians').exists() or u.is_superuser)
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {})

@user_passes_test(lambda u: u.groups.filter(name='Members').exists() or u.is_authenticated)
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {})

# --- Secured Book CRUD Views ---

@permission_required('bookshelf.add_book', raise_exception=True)
@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            # You can uncomment and use the line below if you want to automatically set the user who added the book
            # book.added_by = request.user
            book.save()
            messages.success(request, f"Book '{book.title}' added successfully!")
            return redirect('relationship_app:admin_view') # Or a more appropriate list_books view
        # If form is not valid, the errors will be attached to the form and displayed in the template
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form, 'form_type': 'Add'})


@permission_required('bookshelf.change_book', raise_exception=True)
@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, f"Book '{book.title}' updated successfully!")
            return redirect('relationship_app:admin_view') # Or a more appropriate list_books view
        # If form is not valid, the errors will be attached to the form and displayed in the template
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book, 'form_type': 'Edit'})


@permission_required('bookshelf.delete_book', raise_exception=True)
@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, f"Book '{book.title}' deleted successfully.")
        return redirect('relationship_app:admin_view') # Or a more appropriate list_books view
    return render(request, 'relationship_app/delete_book.html', {'book': book})