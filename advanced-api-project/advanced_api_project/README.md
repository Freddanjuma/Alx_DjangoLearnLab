# Advanced API Project: Book and Author Management

This project implements a robust RESTful API for managing authors and their books using Django and Django REST Framework. It provides comprehensive CRUD (Create, Retrieve, Update, Delete) operations, granular permission handling, advanced filtering, searching, and ordering capabilities, along with custom data validation.

## Project Structure

The core API logic resides within the `api` Django app, which includes:
-   `api/models.py`: Defines the `Author` and `Book` database models with their fields and relationships.
-   `api/serializers.py`: Converts model instances to JSON (serialization) and handles incoming data validation (deserialization). Includes custom field-level and object-level validation.
-   `api/filters.py`: Configures custom filtersets using `django-filter` to enable sophisticated querying of lists of resources.
-   `api/views.py`: Implements API endpoints using Django REST Framework's individual generic views (`ListAPIView`, `RetrieveAPIView`, `CreateAPIView`, `UpdateAPIView`, `DestroyAPIView`) for granular control over each CRUD operation.
-   `api/urls.py`: Defines the URL routes that map HTTP requests to the appropriate API views, including specific patterns required by the project's checking system.

## Features

-   **Granular CRUD Operations:** Separate API endpoints and views are provided for listing, retrieving, creating, updating, and deleting Authors and Books.
-   **Generic Views:** Leverages Django REST Framework's powerful built-in generic views for efficient, concise, and maintainable API development.
-   **Advanced Query Capabilities (for Books):**
    -   **Filtering:** Comprehensive attribute-based filtering for the `Book` list using `django-filter` (e.g., by title, author, publication year).
    -   **Searching:** Full-text search functionality on key `Book` fields (title, author's name, ISBN) using DRF's `SearchFilter`.
    -   **Ordering:** Flexible sorting of `Book` results by multiple fields (e.g., title, publication date) using DRF's `OrderingFilter`.
-   **Permission-Based Access Control:** API endpoints are protected using DRF's permission classes to ensure data integrity and user authorization:
    -   `GET` requests (read operations for list and detail views) are accessible to all users (authenticated or unauthenticated).
    -   `POST`, `PUT`, `PATCH`, `DELETE` requests (write/delete operations) require an authenticated user.
-   **Custom Data Validation:** Serializers incorporate custom validation logic to enforce specific business rules beyond basic model constraints:
    -   `Book`: Title cannot be purely numeric, ISBN must be exactly 13 characters long (if provided), and a book's title must be unique for a given author.
    -   `Author`: Name must be at least 3 characters long.
-   **Custom Response Handling:** Customized `HTTP 204 No Content` deletion responses for Authors and Books provide a user-friendly success message upon successful resource removal.

## API Endpoints

All API endpoints are prefixed with `/api/`.

### Authors

-   **`GET /api/authors/`**:
    -   **Purpose:** List all authors.
    -   **View:** `AuthorListView` (`generics.ListAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Read-only for all users).
    -   **Filtering:** Supports `?name__icontains=value` for case-insensitive partial matching on author names.
-   **`POST /api/authors/create/`**:
    -   **Purpose:** Create a new author.
    -   **View:** `AuthorCreateView` (`generics.CreateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
    -   **Validation:** Custom validation ensures author name is at least 3 characters long.
-   **`GET /api/authors/<int:pk>/`**:
    -   **Purpose:** Retrieve details of a single author by ID.
    -   **View:** `AuthorDetailView` (`generics.RetrieveAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Read-only for all users).
-   **`PUT /api/authors/<int:pk>/update/`**:
    -   **Purpose:** Fully update an existing author by ID.
    -   **View:** `AuthorUpdateView` (`generics.UpdateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
-   **`PATCH /api/authors/<int:pk>/update/`**:
    -   **Purpose:** Partially update an existing author by ID.
    -   **View:** `AuthorUpdateView` (`generics.UpdateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
-   **`DELETE /api/authors/<int:pk>/delete/`**:
    -   **Purpose:** Delete an author by ID.
    -   **View:** `AuthorDeleteView` (`generics.DestroyAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
    -   **Custom Behavior:** Returns a `204 No Content` status with a custom success message upon deletion.

### Books

-   **`GET /api/books/`**:
    -   **Purpose:** List all books with advanced filtering, searching, and ordering capabilities.
    -   **View:** `BookListView` (`generics.ListAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Read-only for all users).
    -   **Query Capabilities:**
        -   **Filtering (Step 1):** Use query parameters for precise attribute matching via `django-filter`.
            -   `?title__icontains=python`: Books with 'python' in their title (case-insensitive partial match).
            -   `?isbn__icontains=978`: Books with '978' in their ISBN (case-insensitive partial match).
            -   `?author=1`: Books by author with ID 1.
            -   `?author_name__icontains=fredd`: Books by authors whose name contains 'fredd' (case-insensitive partial match).
            -   `?published_after=2023-01-01`: Books published on or after January 1, 2023 (YYYY-MM-DD).
            -   `?published_before=2023-12-31`: Books published on or before December 31, 2023 (YYYY-MM-DD).
            -   `?published_date=2023-05-15`: Books published on May 15, 2023 (YYYY-MM-DD).
            -   `?publication_year=2023`: Books published in the year 2023 (YYYY).
        -   **Searching (Step 2):** Use the `search` query parameter for a broader text search across multiple configured fields.
            -   `?search=Django`: Searches for 'Django' in `title`, `author__name`, and `isbn`.
            -   `?search=Learning Python`: Searches for 'Learning Python' in the configured fields.
        -   **Ordering (Step 3):** Use the `ordering` query parameter to sort results by one or more fields.
            -   `?ordering=title`: Sorts by title ascending (A-Z).
            -   `?ordering=-published_date`: Sorts by publication date descending (newest first).
            -   `?ordering=isbn`: Sorts by ISBN ascending.
            -   `?ordering=author__name`: Sorts by author's name ascending.
-   **`POST /api/books/create/`**:
    -   **Purpose:** Create a new book.
    -   **View:** `BookCreateView` (`generics.CreateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
    -   **Validation:** Custom validation ensures title is not purely numeric, ISBN is 13 characters (if provided), and a book's title is unique per author.
-   **`GET /api/books/<int:pk>/`**:
    -   **Purpose:** Retrieve details of a single book by ID.
    -   **View:** `BookDetailView` (`generics.RetrieveAPIView`)
    -   **Permissions:** `permissions.IsAuthenticatedOrReadOnly` (Read-only for all users).
-   **`PUT /api/books/update/<int:pk>/`**:
    -   **Purpose:** Fully update an existing book by ID.
    -   **View:** `BookUpdateView` (`generics.UpdateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
-   **`PATCH /api/books/update/<int:pk>/`**:
    -   **Purpose:** Partially update an existing book by ID.
    -   **View:** `BookUpdateView` (`generics.UpdateAPIView`)
    -   **Permissions:** `permissions.IsAuthenticated` (Requires authentication).
-   **`DELETE /api/books/delete/<int:pk>/`**:
    -   **Purpose:** Delete a book by ID.
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
    pip install django djangorestframework django-filter
    ```

4.  **Apply Database Migrations:**
    ```bash
    # Ensure you are in the advanced-api-project directory
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

-   **Browsable API:** Access `http://127.0.0.1:8000/api/authors/` or `http://127.0.0.1:8000/api/books/` (or any other defined endpoint) in your browser.
    -   **GET Requests:** Test directly in the browser, including the new filtering, searching, and ordering query parameters.
    -   **POST, PUT, PATCH, DELETE Requests:** Log in using the top-right corner form with your superuser credentials to perform these operations via the browsable API forms.
-   **Command-line (curl) / Postman:**
    -   **GET (unauthenticated):**
        ```bash
        curl "[http://127.0.0.1:8000/api/books/?search=django&ordering=-published_date](http://127.0.0.1:8000/api/books/?search=django&ordering=-published_date)"
        ```
    -   **POST/PUT/PATCH/DELETE (requires authentication):** For testing write operations via `curl` or Postman, you would typically need to implement token-based authentication (e.g., obtain a token from `/api-token-auth/` if `rest_framework.authtoken` is configured) and include it in your request headers. For simplicity in this task, comprehensive testing via the browsable API after superuser login is often sufficient to demonstrate permissions.
-   **Permissions Enforcement:**
    -   Verify that `POST`, `PUT`, `PATCH`, `DELETE` requests fail with `403 Forbidden` if you are not logged in.
    -   Confirm these operations succeed after successful authentication.
-   **Validation Checks:**
    -   Test serializer validation by attempting to create an author with a very short name (less than 3 characters).
    -   Attempt to create a book with a purely numeric title (e.g., "123").
    -   Try creating a book with an ISBN that is not 13 characters long.
    -   Attempt to create a book with the same title and author as an existing book.
    All these should return validation errors (e.g., `400 Bad Request`).

---