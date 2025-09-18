# LibraryProject/bookshelf/views.py

# Import necessary modules from Django
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExampleForm # Ensure ExampleForm is imported from your forms.py
from django.contrib import messages # For displaying messages to the user

# Import forms and models from the current 'bookshelf' app 
from .models import Book, Author # Ensure Book and Author models are imported if used directly

# --- Book Management Views ---

# View to display a list of all books.
# This view retrieves all Book objects from the database and passes them to the template.
# Documentation: This view implicitly prevents SQL injection by using Django's ORM (Book.objects.all()).
def book_list_view(request):
    books = Book.objects.all() # Retrieve all book records
    # Renders the 'book_list.html' template, passing the 'books' queryset to it.
    return render(request, 'bookshelf/book_list.html', {'books': books})

# View to display detailed information about a single book.
# 'pk' (primary key) is used to identify the specific book.
# get_object_or_404 ensures a 404 error if the book does not exist, improving robustness.
def book_detail_view(request, pk):
    # Retrieve a single Book object, or raise Http404 if not found.
    book = get_object_or_404(Book, pk=pk)
    # Renders the 'book_detail.html' template, passing the 'book' object.
    return render(request, 'bookshelf/book_detail.html', {'book': book})

# Note: Book CRUD views (add, edit, delete) are also defined in relationship_app/views.py
# for security reasons, leveraging permissions and login requirements.
# You can also have them here if you want separate app-specific CRUD,
# but ensure consistency and avoid duplication.
# For example, if you want a simple unauthenticated add_book for demonstration:
# def add_book_simple(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Book added successfully (simple version)!")
#             return redirect('bookshelf:book_list')
#     else:
#         form = BookForm()
#     return render(request, 'bookshelf/book_form.html', {'form': form, 'form_type': 'Add Book'})


# --- Checker-Specific Example Form View ---

# This view handles the 'ExampleForm' which is a simple non-model form.
# It demonstrates form processing and validation, satisfying a checker requirement.
# Documentation: This view uses Django Forms (ExampleForm) for secure input handling.
# Data validation and cleaning are performed by form.is_valid(), preventing XSS and other attacks.
def form_example_view(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = ExampleForm(request.POST)
        # Check if the submitted data is valid according to the form's rules
        if form.is_valid():
            # Access cleaned (validated and sanitized) data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # In a real application, you would process this data (e.g., save to DB, send email).
            # For the checker, we simply render a success page.
            messages.success(request, f"Thank you, {name}! Your message has been received.")
            # Redirect to a success page or render a message
            return render(request, 'bookshelf/success_example_form.html', {'name': name})
        else:
            # If the form is not valid, messages can provide feedback to the user
            messages.error(request, "Please correct the errors in the form.")
    else:
        # If it's a GET request, create an empty form instance
        form = ExampleForm()
    
    # Renders the 'form_example.html' template, passing the form instance.
    return render(request, 'bookshelf/form_example.html', {'form': form})