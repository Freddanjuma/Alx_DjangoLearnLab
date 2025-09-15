# bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from .models import Book, Author
from .forms import BookForm


# --- Basic Views (accessible to logged-in users) ---
@login_required
def book_list(request):
    """
    Displays a list of all books. Requires user to be logged in.
    Note: For simplicity, all logged-in users can see the list.
    More granular 'can_view_book' can be enforced if specific books are sensitive.
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@login_required
def book_detail(request, pk):
    """
    Displays details for a single book. Requires user to be logged in.
    Similar to book_list, 'can_view_book' is implicitly handled by showing this view
    to logged-in users. Could be made more restrictive if needed.
    """
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_detail.html', {'book': book})


# --- Permission-Protected Views for Book CRUD Operations ---

@permission_required('bookshelf.can_create_book', raise_exception=True)
def book_create(request):
    """
    Handles the creation of new book instances.
    This view is protected by the 'bookshelf.can_create_book' permission.
    Users must belong to a group with this permission (e.g., 'Admins', 'Editors')
    to access this view. If permission is denied, a 403 Forbidden error is raised.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully!')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form, 'form_type': 'Create'})

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def book_edit(request, pk):
    """
    Handles editing an existing book instance.
    Protected by the 'bookshelf.can_edit_book' permission.
    Users must belong to a group with this permission (e.g., 'Admins', 'Editors')
    to access this view. If permission is denied, a 403 Forbidden error is raised.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'Book "{book.title}" updated successfully!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form, 'book': book, 'form_type': 'Edit'})

@permission_required('bookshelf.can_delete_book', raise_exception=True)
def book_delete(request, pk):
    """
    Handles the deletion of a book instance.
    Protected by the 'bookshelf.can_delete_book' permission.
    Users must belong to a group with this permission (e.g., 'Admins')
    to access this view. If permission is denied, a 403 Forbidden error is raised.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, f'Book "{book.title}" deleted successfully!')
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})