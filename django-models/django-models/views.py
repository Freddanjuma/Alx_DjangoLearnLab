from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Helper functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "django-models/admin_view.html")


# Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "django-models/librarian_view.html")


# Member View
@user_passes_test(is_member)
def member_view(request):
    return render(request, "django-models/member_view.html")
