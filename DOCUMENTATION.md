# Django Blog Authentication System Documentation

This document provides an overview, setup instructions, and usage guide for the authentication system implemented in the `django_blog` project.

## 1. Project Overview

The `django_blog` project now includes robust user authentication, covering registration, login, logout, and a basic user profile management system. This functionality is built using Django's powerful built-in authentication system combined with custom views and forms where necessary.

## 2. Setup Instructions

These instructions assume you have already followed the initial project setup steps (virtual environment, Django installation, `blog` app creation, basic URL/template configuration).

### 2.1. Code Structure

Ensure your project structure includes the following key files:

-   `django_blog/blog/forms.py`: Contains custom forms for user creation and modification.
-   `django_blog/blog/views.py`: Includes `register_view` (custom) and `profile_view` (custom, protected).
-   `django_blog/blog/urls.py`: Defines URL patterns for authentication and profile management.
-   `django_blog/templates/blog/`: Contains HTML templates for `login.html`, `register.html`, `logged_out.html`, `profile.html`, and the updated `base.html`.
-   `django_blog/django_blog/settings.py`: Updated with authentication-related settings (redirect URLs, message tags).

### 2.2. Database Migrations

After integrating the authentication code, run migrations to ensure your database schema is up-to-date with Django's user model requirements.

```bash
python manage.py makemigrations blog
python manage.py migrate

2.3. Static Files
Ensure static files are collected and served correctly for styling the authentication forms. The base.html links to styles.css and scripts.js from the static directory within django_blog/.

3. Authentication System Details
3.1. User Registration
View: blog.views.register_view (custom)

Form: blog.forms.CustomUserCreationForm

Extends Django's UserCreationForm to include email (required), first_name, and last_name.

Template: blog/register.html

URL: /register/ (named register)

Security: Utilizes {% csrf_token %} for CSRF protection. Passwords are automatically hashed by UserCreationForm.

3.2. User Login
View: django.contrib.auth.views.LoginView (built-in)

Template: blog/login.html

URL: /login/ (named login)

Security: {% csrf_token %} is used in the template. Handles password verification securely.

Redirect: Upon successful login, users are redirected to the URL defined by LOGIN_REDIRECT_URL in settings.py (e.g., 'home').

3.3. User Logout
View: django.contrib.auth.views.LogoutView (built-in)

Template: blog/logged_out.html

URL: /logout/ (named logout)

Redirect: Upon successful logout, users are redirected to the URL defined by LOGOUT_REDIRECT_URL in settings.py (e.g., 'home').

3.4. Profile Management
View: blog.views.profile_view (custom)

Decorated with @login_required to restrict access to authenticated users.

Handles GET requests to display the user's current profile details and a pre-filled editing form.

Handles POST requests to validate and save updated user information.

Form: blog.forms.CustomUserChangeForm

Used for editing core User model fields: username, email, first_name, last_name.

Template: blog/profile.html

URL: /profile/ (named profile)

Security: {% csrf_token %} is used in the form.

4. Security Measures
CSRF Protection: All forms (login, register, profile editing) include {% csrf_token %} to prevent Cross-Site Request Forgery attacks.

Password Hashing: Django's built-in authentication system automatically handles password hashing using strong, industry-standard algorithms, ensuring passwords are never stored in plain text.

Login Required: Sensitive views like the profile page are protected using the @login_required decorator, ensuring only authenticated users can access them.

5. User Guide
5.1. Accessing the Blog
Start the Django development server: python manage.py runserver

Open your web browser and navigate to http://127.0.0.1:8000/.

5.2. Creating an Account (Register)
Click on the "Register" link in the navigation bar.

Fill out the registration form, providing a unique username, a valid email address, a password (and confirmation), and optionally your first and last name.

Click "Register".

Upon successful registration, you will be redirected to the login page with a success message.

5.3. Logging In
Click on the "Login" link in the navigation bar, or you will be automatically redirected there after registration.

Enter your username and password.

Click "Login".

You will be redirected to the homepage, and the navigation bar will now show "Profile" and "Logout" links.

5.4. Viewing and Editing Your Profile
Once logged in, click on the "Profile" link in the navigation bar.

You will see your current profile details and a form pre-filled with your information.

Modify any fields you wish to change (e.g., email, first name, last name).

Click "Update Profile".

Your changes will be saved, and you will see a success message.

5.5. Logging Out
While logged in, click on the "Logout" link in the navigation bar.

You will be logged out and redirected to the homepage, displaying a "You have been logged out" message, and the navigation links will revert to "Login" and "Register".

