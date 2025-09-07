from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from .models import Book, Library

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

# View for user registration - FIXED TEMPLATE PATH
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('relationship_app:all-books')  #  app namespace
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})  # FIXED PATH

# ADD THIS: Custom login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('relationship_app:all-books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# ADD THIS: Profile view
@login_required
def profile(request):
    return render(request, 'relationship_app/profile.html', {'user': request.user})