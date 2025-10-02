from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import date, timedelta

from .models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Comprehensive test suite for the Book API endpoints, covering CRUD operations,
    permissions, filtering, searching, and ordering functionalities.
    """

    def setUp(self):
        """
        Set up initial test data and URLs for all test methods.
        This includes creating test users, authors, and multiple books
        with diverse and FIXED dates to facilitate thorough and deterministic testing
        of query capabilities.
        """
        # 1. Create a superuser for authenticated requests
        self.user = User.objects.create_superuser(username='testuser', email='test@example.com', password='password123')
        # APITestCase client is already logged in from setUp by default
        self.client.login(username='testuser', password='password123')

        # 2. Create test authors
        self.author1 = Author.objects.create(name='John Doe')
        self.author2 = Author.objects.create(name='Jane Smith')
        self.author3 = Author.objects.create(name='Alice Wonderland')

        # 3. Create test books with diverse and FIXED dates for deterministic filtering/searching/ordering
        # Using fixed dates avoids issues with `date.today()` changing the test outcomes.
        
        self.book1 = Book.objects.create(
            title='Learning Python',
            isbn='9781234567890',
            published_date=date(2022, 1, 1), # Fixed to 2022
            author=self.author1,
        )
        self.book2 = Book.objects.create(
            title='Django REST Framework Handbook',
            isbn='9780987654321',
            published_date=date(2021, 5, 15), # Fixed to 2021
            author=self.author2,
        )
        self.book3 = Book.objects.create(
            title='Advanced Algorithms',
            isbn='9781122334455',
            published_date=date(2024, 3, 10), # Fixed to 2024
            author=self.author1,
        )
        self.book4 = Book.objects.create(
            title='Data Structures in Python',
            isbn='9785566778899',
            published_date=date(2022, 11, 20), # Fixed to 2022
            author=self.author2,
        )
        self.book5 = Book.objects.create(
            title='The 2023 Guide',
            isbn='9782023000000',
            published_date=date(2023, 6, 15), # Fixed to 2023 - ONLY book in 2023
            author=self.author3,
        )
        self.book6 = Book.objects.create(
            title='Future Tech 2025',
            isbn='9782025000000',
            published_date=date(2025, 1, 1), # Fixed to 2025
            author=self.author3,
        )

        # 4. Define URLs using reverse for each endpoint
        # The URL names must match those defined in api/urls.py
        self.book_list_url = reverse('book-list')
        self.book_create_url = reverse('book-create')
        self.book_detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})
        self.book_update_url = lambda pk: reverse('book-update', kwargs={'pk': pk})
        self.book_delete_url = lambda pk: reverse('book-delete', kwargs={'pk': pk})

    # --- Test Permissions & CRUD for Books ---

    def test_get_book_list_unauthenticated(self):
        """
        Ensure unauthenticated users can retrieve the list of books.
        """
        self.client.logout() # Explicitly log out for this test
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Book.objects.count()) # Should return all books

    def test_get_book_detail_unauthenticated(self):
        """
        Ensure unauthenticated users can retrieve details of a single book.
        """
        self.client.logout()
        response = self.client.get(self.book_detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_authenticated_success(self):
        """
        Ensure authenticated users can create a new book.
        """
        data = {
            'title': 'New Test Book',
            'isbn': '9789999999999',
            'published_date': '2024-01-01',
            'author': self.author1.pk,
        }
        # APITestCase client is already logged in from setUp by default
        response = self.client.post(self.book_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 7) # 6 initial + 1 new
        self.assertEqual(Book.objects.get(title='New Test Book').author, self.author1)

    def test_create_book_unauthenticated_fails(self):
        """
        Ensure unauthenticated users cannot create a new book.
        """
        self.client.logout()
        data = {
            'title': 'Unauthorized Book',
            'isbn': '9780000000000',
            'published_date': '2024-02-01',
            'author': self.author1.pk,
        }
        response = self.client.post(self.book_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) # IsAuthenticatedOrReadOnly
        self.assertEqual(Book.objects.count(), 6) # Should remain 6

    def test_update_book_authenticated_success(self):
        """
        Ensure authenticated users can update an existing book.
        """
        updated_title = 'Updated Python Book'
        data = {'title': updated_title}
        response = self.client.patch(self.book_update_url(self.book1.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, updated_title)

    def test_update_book_unauthenticated_fails(self):
        """
        Ensure unauthenticated users cannot update a book.
        """
        self.client.logout()
        data = {'title': 'Attempted Update'}
        response = self.client.patch(self.book_update_url(self.book1.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) # IsAuthenticatedOrReadOnly
        self.book1.refresh_from_db()
        self.assertNotEqual(self.book1.title, 'Attempted Update')

    def test_delete_book_authenticated_success(self):
        """
        Ensure authenticated users can delete a book.
        """
        response = self.client.delete(self.book_delete_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 5) # 6 initial - 1 deleted
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(pk=self.book1.pk)

    def test_delete_book_unauthenticated_fails(self):
        """
        Ensure unauthenticated users cannot delete a book.
        """
        self.client.logout()
        response = self.client.delete(self.book_delete_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) # IsAuthenticatedOrReadOnly
        self.assertEqual(Book.objects.count(), 6) # Should remain 6

    # --- Test Filtering Functionality ---

    def test_filter_by_title_icontains(self):
        """
        Test filtering books by a partial, case-insensitive title match.
        """
        response = self.client.get(self.book_list_url + '?title__icontains=python')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) # Learning Python, Data Structures in Python
        self.assertIn(self.book1.title, [book['title'] for book in response.data])
        self.assertIn(self.book4.title, [book['title'] for book in response.data])

    def test_filter_by_author_id(self):
        """
        Test filtering books by author ID.
        """
        response = self.client.get(self.book_list_url + f'?author={self.author1.pk}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) # Learning Python, Advanced Algorithms
        self.assertIn(self.book1.title, [book['title'] for book in response.data])
        self.assertIn(self.book3.title, [book['title'] for book in response.data])

    def test_filter_by_author_name_icontains(self):
        """
        Test filtering books by partial, case-insensitive author name match.
        """
        response = self.client.get(self.book_list_url + '?author_name__icontains=john')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) # Learning Python, Advanced Algorithms (by John Doe)
        self.assertIn(self.book1.title, [book['title'] for book in response.data])
        self.assertIn(self.book3.title, [book['title'] for book in response.data])

    def test_filter_by_publication_year(self):
        """
        Test filtering books by a specific publication year.
        """
        response = self.client.get(self.book_list_url + '?publication_year=2023')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) # Only book5 is 2023
        self.assertEqual(response.data[0]['title'], self.book5.title)

    def test_filter_by_published_after(self):
        """
        Test filtering books published on or after a specific date.
        Using book4.published_date (2022-11-20)
        Expected: book3 (2024), book4 (2022-11-20), book5 (2023), book6 (2025)
        """
        response = self.client.get(self.book_list_url + f'?published_after={self.book4.published_date.strftime("%Y-%m-%d")}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Books published on or after 2022-11-20
        expected_books = [self.book3, self.book4, self.book5, self.book6] 
        expected_titles = sorted([book.title for book in expected_books])
        actual_titles = sorted([book['title'] for book in response.data])
        
        self.assertEqual(actual_titles, expected_titles)
        self.assertEqual(len(response.data), 4)

    def test_filter_by_published_before(self):
        """
        Test filtering books published on or before a specific date.
        Using book4.published_date (2022-11-20)
        Expected: book1 (2022-01-01), book2 (2021-05-15), book4 (2022-11-20)
        """
        response = self.client.get(self.book_list_url + f'?published_before={self.book4.published_date.strftime("%Y-%m-%d")}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Books published on or before 2022-11-20
        expected_books = [self.book1, self.book2, self.book4] 
        expected_titles = sorted([book.title for book in expected_books])
        actual_titles = sorted([book['title'] for book in response.data])
        
        self.assertEqual(actual_titles, expected_titles)
        self.assertEqual(len(response.data), 3)

    # --- Test Search Functionality ---

    def test_search_by_book_title(self):
        """
        Test searching by a term present in book titles.
        """
        response = self.client.get(self.book_list_url + '?search=python')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) # Learning Python, Data Structures in Python
        self.assertIn(self.book1.title, [book['title'] for book in response.data])
        self.assertIn(self.book4.title, [book['title'] for book in response.data])

    def test_search_by_author_name(self):
        """
        Test searching by a term present in author names.
        """
        response = self.client.get(self.book_list_url + '?search=john')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn(self.book1.title, [book['title'] for book in response.data]) # By John Doe
        self.assertIn(self.book3.title, [book['title'] for book in response.data]) # By John Doe

    def test_search_by_isbn(self):
        """
        Test searching by a term present in ISBNs.
        """
        response = self.client.get(self.book_list_url + '?search=97809')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book2.title) # Django REST Framework Handbook

    # --- Test Ordering Functionality ---

    def test_order_by_title_ascending(self):
        """
        Test ordering books by title in ascending order.
        """
        response = self.client.get(self.book_list_url + '?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        actual_titles = [book['title'] for book in response.data]
        all_books = [self.book1, self.book2, self.book3, self.book4, self.book5, self.book6]
        expected_sorted_titles = [book.title for book in sorted(all_books, key=lambda b: b.title)]
        self.assertEqual(actual_titles, expected_sorted_titles)

    def test_order_by_title_descending(self):
        """
        Test ordering books by title in descending order.
        """
        response = self.client.get(self.book_list_url + '?ordering=-title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        actual_titles = [book['title'] for book in response.data]
        all_books = [self.book1, self.book2, self.book3, self.book4, self.book5, self.book6]
        expected_sorted_titles = [book.title for book in sorted(all_books, key=lambda b: b.title, reverse=True)]
        self.assertEqual(actual_titles, expected_sorted_titles)

    def test_order_by_published_date_ascending(self):
        """
        Test ordering books by published date in ascending order.
        """
        response = self.client.get(self.book_list_url + '?ordering=published_date')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        actual_titles_in_order = [book['title'] for book in response.data]
        all_books = [self.book1, self.book2, self.book3, self.book4, self.book5, self.book6]
        expected_sorted_titles = [book.title for book in sorted(all_books, key=lambda b: b.published_date)]
        self.assertEqual(actual_titles_in_order, expected_sorted_titles)

    def test_order_by_published_date_descending(self):
        """
        Test ordering books by published date in descending order.
        """
        response = self.client.get(self.book_list_url + '?ordering=-published_date')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        actual_titles_in_order = [book['title'] for book in response.data]
        all_books = [self.book1, self.book2, self.book3, self.book4, self.book5, self.book6]
        expected_sorted_titles = [book.title for book in sorted(all_books, key=lambda b: b.published_date, reverse=True)]
        self.assertEqual(actual_titles_in_order, expected_sorted_titles)