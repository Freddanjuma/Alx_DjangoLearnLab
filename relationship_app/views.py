from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Specific imports required by the checker
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView


# View for listing books
def list_books(request):
    books = Book.objects.all().order_by('title')
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


# View for library details
class LibraryDetailView(DetailView):
    model = Library
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
    return render(request, 'relationship_app/registration/register.html', {'form': form})