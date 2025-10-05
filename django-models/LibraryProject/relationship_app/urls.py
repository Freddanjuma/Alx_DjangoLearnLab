from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  

app_name = "relationship_app"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("profile/", views.profile_view, name="profile"),

    # Role-based views
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),

    # Secured book CRUD views
    path("add_book/", views.add_book, name="add_book"),
    path("editbook/<int:pk>/", views.edit.book, name="edit_book"),
    path("delete-book/<int:pk>/", views.delete.book, name="delete_book"),
]
