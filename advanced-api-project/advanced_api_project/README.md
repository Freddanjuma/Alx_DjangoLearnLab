# Advanced API Project: Book and Author Management

This project implements a RESTful API for managing authors and their books using Django and Django REST Framework. It provides robust CRUD (Create, Retrieve, Update, Delete) operations, granular permission handling, advanced filtering capabilities, and custom data validation.

## Project Structure

The core API logic resides within the `api` Django app, which includes:
-   `api/models.py`: Defines the `Author` and `Book` database models with their fields and relationships.
-   `api/serializers.py`: Converts model instances to JSON (serialization) and handles incoming data validation (deserialization). Includes custom field-level and object-level validation.
-   `api/filters.py`: Configures custom filters using `django-filter` to enable sophisticated querying of lists of resources.
-   `api/views.py`: Implements API endpoints using Django REST Framework's individual generic views (`ListAPIView`, `RetrieveAPIView`, `CreateAPIView`, `UpdateAPIView`, `DestroyAPIView`) for granular control over each CRUD operation.
-   `api/urls.py`: Defines the URL routes that map HTTP requests to the appropriate API views.

## Features

-   **Granular CRUD Operations:** Separate API endpoints and views for listing, retrieving, creating, updating, and deleting Authors and Books.
-   **Generic Views:** Leverages DRF's built-in generic views for efficient and maintainable API development.
-   **Advanced Filtering:** Provides flexible filtering options for `Book` and `Author` listings using `django-filter`.
    -   **Books:** Filterable by `title` (partial, case-insensitive), `author` (ID), `author_name` (partial, case-insensitive), `isbn` (partial, case-insensitive), `published_date` (exact, or range using `__gte`, `__lte`).
    -   **Authors:** Filterable by `name` (partial, case-insensitive).
-   **Permission-Based Access Control:** API endpoints are protected using DRF's permission classes.
    -   `GET` requests (read operations for list and detail views) are accessible to all users (authenticated or unauthenticated).
    -   `POST`, `PUT`, `PATCH`, `DELETE` requests (write/delete operations) require an authenticated user.
-   **Custom Data Validation:** Serializers incorporate custom validation logic to enforce business rules beyond basic model constraints:
    -   `Book`: Title cannot be purely numeric, ISBN must be exactly 13 characters (if provided), and a book's title must be unique for a given author.
    -   `Author`: Name must be at least 3 characters long.
-   **Custom Response Handling:** Customized `HTTP 204 No Content` deletion responses for Authors and Books provide a user-friendly success message.

## API Endpoints

All API endpoints are prefixed with `/api/`.

### Authors

-   **`GET /api/authors/`**:
    -   **Purpose:** List all authors.
    -   **View:** `AuthorListView` (`generics.ListAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Read-only for all users).
    -   **Filtering:** Supports `?name__icontains=value`
-   **`POST /api/authors/create/`**:
    -   **Purpose:** Create a new author.
    -   **View:** `AuthorCreateView` (`generics.CreateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
    -   **Validation:** Custom validation ensures author name is at least 3 characters long.
-   **`GET /api/authors/<int:pk>/`**:
    -   **Purpose:** Retrieve details of a single author.
    -   **View:** `AuthorDetailView` (`generics.RetrieveAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Read-only for all users).
-   **`PUT /api/authors/<int:pk>/update/`**:
    -   **Purpose:** Fully update an existing author.
    -   **View:** `AuthorUpdateView` (`generics.UpdateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
-   **`PATCH /api/authors/<int:pk>/update/`**:
    -   **Purpose:** Partially update an existing author.
    -   **View:** `AuthorUpdateView` (`generics.UpdateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
-   **`DELETE /api/authors/<int:pk>/delete/`**:
    -   **Purpose:** Delete an author.
    -   **View:** `AuthorDeleteView` (`generics.DestroyAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
    -   **Custom Behavior:** Returns a `204 No Content` status with a custom success message upon deletion.

### Books

-   **`GET /api/books/`**:
    -   **Purpose:** List all books.
    -   **View:** `BookListView` (`generics.ListAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Read-only for all users).
    -   **Filtering Examples:**
        -   `?title__icontains=python`
        -   `?author=1` (filter by author ID)
        -   `?author_name__icontains=fredd`
        -   `?isbn__icontains=123`
        -   `?published_after=2023-01-01`
        -   `?published_before=2024-01-01`
        -   `?published_date=2023-05-15`
-   **`POST /api/books/create/`**:
    -   **Purpose:** Create a new book.
    -   **View:** `BookCreateView` (`generics.CreateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
    -   **Validation:** Custom validation ensures title is not purely numeric, ISBN is 13 characters (if provided), and a book's title is unique per author.
-   **`GET /api/books/<int:pk>/`**:
    -   **Purpose:** Retrieve details of a single book.
    -   **View:** `BookDetailView` (`generics.RetrieveAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Read-only for all users).
-   **`PUT /api/books/<int:pk>/update/`**:
    -   **Purpose:** Fully update an existing book.
    -   **View:** `BookUpdateView` (`generics.UpdateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
-   **`PATCH /api/books/<int:pk>/update/`**:
    -   **Purpose:** Partially update an existing book.
    -   **View:** `BookUpdateView` (`generics.UpdateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
-   **`DELETE /api/books/<int:pk>/delete/`**:
    -   **Purpose:** Delete a book.
    -   **View:** `BookDeleteView` (`generics.DestroyAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
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
    pip install django djangorest