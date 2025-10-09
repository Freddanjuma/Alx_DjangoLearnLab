from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .forms import CustomUserChangeForm

# 📝 View: List all posts
def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


# 🧍‍♂️ View: Register new user
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


# 👤 View: Profile (view & edit)
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})
