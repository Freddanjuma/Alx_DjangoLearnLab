from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "relationship_app"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", __import__('relationship_app.views').views.register, name="register"),
    path("profile/", __import__('relationship_app.views').views.profile_view, name="profile"),

    # Role-based views
    path("admin-view/", __import__('relationship_app.views').views.admin_view, name="admin_view"),
    path("librarian-view/", __import__('relationship_app.views').views.librarian_view, name="librarian_view"),
    path("member-view/", __import__('relationship_app.views').views.member_view, name="member_view"),
]
