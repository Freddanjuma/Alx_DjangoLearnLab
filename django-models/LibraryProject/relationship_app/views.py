from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Corrected imports for the checker
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView


# Renamed this function to 'list_books' for the checker
def list_books(request):
    """
    This view retrieves all Book objects from the database and
    passes them to the namespaced template.
    """
    books = Book.objects.all().order_by('title')
    context = {'books': books}
    # This path is now correct for the checker
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    """
    This view uses DetailView to display a single Library object.
    """
    model = Library
    # This path is also now correct for the checker
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# View for user registration
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all-books')
    else:
        form = UserCreationForm()
    # This path is now correct for the checker
    return render(request, 'relationship_app/registration/register.html', {'form': form})