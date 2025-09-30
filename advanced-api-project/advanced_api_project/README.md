# Advanced API Project: Book and Author Management

This project implements a RESTful API for managing authors and their books using Django and Django REST Framework. It provides robust CRUD (Create, Retrieve, Update, Delete) operations, filtering capabilities, and appropriate permission handling.

## Project Structure

The core API logic resides within the `api` Django app, which includes:
-   `api/models.py`: Defines the `Author` and `Book` database models.
-   `api/serializers.py`: Converts model instances to JSON and validates incoming data.
-   `api/filters.py`: Configures custom filters using `django-filter` for enhanced query capabilities.
-   `api/views.py`: Implements API endpoints using Django REST Framework's generic views.
-   `api/urls.py`: Defines the URL routes for the API endpoints.

## Features

-   **CRUD Operations:** Full support for creating, reading, updating, and deleting Authors and Books.
-   **Generic Views:** Utilizes DRF's `ListCreateAPIView` and `RetrieveUpdateDestroyAPIView` for efficient and concise view implementation.
-   **Filtering:** Advanced filtering for `Book` and `Author` listings using `django-filter`.
    -   Books can be filtered by `title` (partial, case-insensitive), `author` (ID), `author_name` (partial, case-insensitive), `isbn` (exact or partial), and `published_date` (exact or range).
    -   Authors can be filtered by `name` (partial, case-insensitive).
-   **Permissions:** API endpoints are protected to ensure data integrity and user authorization.
    -   Read-only operations (GET) are accessible to all users (authenticated or unauthenticated).
    -   Write operations (POST, PUT, PATCH, DELETE) require user authentication.
-   **Custom Validation:** Serializers include custom validation logic to enforce specific business rules (e.g., book titles not purely numeric, ISBN length, unique book titles per author).
-   **Custom Response Handling:** Customized deletion responses for better API feedback.

## API Endpoints

All API endpoints are prefixed with `/api/`.

### Authors

-   **`GET /api/authors/`**:
    -   **Purpose:** List all authors.
    -   **View:** `AuthorListCreateView` (`generics.ListCreateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Read-only for all, creation requires authentication).
    -   **Filtering:** Supports `?name__icontains=value`
-   **`POST /api/authors/`**:
    -   **Purpose:** Create a new author.
    -   **View:** `AuthorListCreateView` (`generics.ListCreateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Requires authentication).
    -   **Validation:** Custom validation ensures author name is at least 3 characters long.
-   **`GET /api/authors/<int:pk>/`**:
    -   **Purpose:** Retrieve details of a single author.
    -   **View:** `AuthorRetrieveUpdateDestroyView` (`generics.RetrieveUpdateDestroyAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Read-only for all).
-   **`PUT /api/authors/<int:pk>/`**:
    -   **Purpose:** Fully update an existing author.
    -   **View:** `AuthorRetrieveUpdateDestroyView` (`generics.RetrieveUpdateDestroyAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Requires authentication).
-   **`PATCH /api/authors/<int:pk>/`**:
    -   **Purpose:** Partially update an existing author.
    -   **View:** `AuthorRetrieveUpdateDestroyView` (`generics.RetrieveUpdateDestroyAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Requires authentication).
-   **`DELETE /api/authors/<int:pk>/`**:
    -   **Purpose:** Delete an author.
    -   **View:** `AuthorRetrieveUpdateDestroyView` (`generics.RetrieveUpdateDestroyAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Requires authentication).
    -   **Custom Behavior:** Returns a `204 No Content` status with a custom success message upon deletion.

### Books

-   **`GET /api/books/`**:
    -   **Purpose:** List all books.
    -   **View:** `BookListCreateView` (`generics.ListCreateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Read-only for all, creation requires authentication).
    -   **Filtering Examples:**
        -   `?title__icontains=python`
        -   `?author=1` (filter by author ID)
        -   `?author_name__icontains=fredd`
        -   `?isbn__icontains=123`
        -   `?published_after=2023-01-01`
        -   `?published_before=2024-01-01`
        -   `?published_date=2023-05-15`
-   **`POST /api/books/`**:
    -   **Purpose:** Create a new book.
    -   **View:** `BookListCreateView` (`generics.ListCreateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Requires authentication).
    -   **Validation:** Custom validation ensures title is not purely numeric, ISBN is 13 characters (if provided), and title is unique per author.
-   **`GET /api/books/<int:pk>/`**:
    -   **Purpose:** Retrieve details of a single book.
    -   **View:** `BookRetrieveUpdateDestroyView` (`generics.RetrieveUpdateDestroyAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Read-only for all).
-   **`PUT /api/books/<int:pk>/`**:
    -   **Purpose:** Fully update an existing book.
    -   **View:** `BookRetrieveUpdateDestroyView` (`generics.RetrieveUpdateDestroyAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Requires authentication).
-   **`PATCH /api/books/<int:pk>/`**:
    -   **Purpose:** Partially update an existing book.
    -   **View:** `BookRetrieveUpdateDestroyView` (`generics.RetrieveUpdateDestroyAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Requires authentication).
-   **`DELETE /api/books/<int:pk>/`**:
    -   **Purpose:** Delete a book.
    -   **View:** `BookRetrieveUpdateDestroyView` (`generics.RetrieveUpdateDestroyAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Requires authentication).
    -   **Custom Behavior:** Returns a `204 No Content` status with a custom success message upon deletion.

## Setup and Local Development

To run this project locally:

1.  **Clone the Monorepo:**
    ```bash
    git clone [https://github.com/Freddanjuma/Alx_DjangoLearnLab.git](https://github.com/Freddanjuma/Alx_DjangoLearnLab.git)
    cd Alx_DjangoLearnLab/advanced-api-project
    ```
    *(Adjust the path if your local setup is different)*

2.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/Scripts/activate # On Windows (Git Bash/MINGW64)
    # OR: source venv/bin/activate # On Linux/macOS
    ```

3.  **Install Dependencies:**
    ```bash
    pip install django djangorestframework django-filter
    ```

4.  **Apply Database Migrations:**
    ```bash
    python manage.py makemigrations api
    python manage.py migrate
    ```

5.  **Create a Superuser (for Admin panel and authenticated testing):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create your superuser credentials.

6.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

    The API will be available at `http://127.0.0.1:8000/api/`.

## Testing the API

-   **Browsable API:** Access `http://127.0.0.1:8000/api/authors/` or `http://127.0.0.1:8000/api/books/` in your browser. You can test GET requests directly. For POST, PUT, DELETE, log in using the top-right corner form with your superuser credentials.
-   **Command-line (curl):**
    -   **GET (unauthenticated):**
        ```bash
        curl [http://127.0.0.1:8000/api/books/](http://127.0.0.1:8000/api/books/)
        ```
    -   **POST (requires authentication token or session):** For actual testing via `curl` or Postman, you'd typically need to obtain an authentication token first. For the purpose of this task, testing via the browsable API after logging in with the superuser is sufficient to demonstrate permissions.
-   **Permissions:** Verify that `POST`, `PUT`, `PATCH`, `DELETE` requests fail with `403 Forbidden` if you are not logged in, but succeed after authentication.
-   **Validation:** Test serializer validation by attempting to create an author with a very short name or a book with a purely numeric title (if you implemented those specific custom validations).

---