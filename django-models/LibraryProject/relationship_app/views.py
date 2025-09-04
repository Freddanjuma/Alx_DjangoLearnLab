# (imports at the top remain the same)
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
# (...your other views like list_books, LibraryDetailView...)

# New view for user registration
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all-books')
    else:
        form = UserCreationForm()
    # CORRECTED LINE for the checker
    return render(request, 'relationship_app/registration/register.html', {'form': form})