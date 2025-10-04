# django_blog/blog/views.py

from django.shortcuts import render

def home_view(request):
    return render(request, 'blog/base.html', {})

def post_list_view(request):
    return render(request, 'blog/post_list.html', {})

# Ensure these two functions are present and correctly defined
def login_view(request):
    return render(request, 'blog/login.html', {})

def register_view(request):
    return render(request, 'blog/register.html', {})
    