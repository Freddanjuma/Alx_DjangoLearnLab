# relationship_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "relationship_app"

urlpatterns = [
    path("register/", views.register_view, name="register"), # This was the missing link!
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("profile/", views.profile_view, name="profile"),

    # Role-based views
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),

    # Secured book CRUD views
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/<int:pk>/", views.edit_book, name="edit_book"),
    path("delete_book/<int:pk>/", views.delete_book, name="delete_book"),
    # You might also want a path for listing books, e.g.:
    # path("books/", views.list_books, name="list_books"),
]
