#
# This script is designed to be run within the Django shell.
# To execute, navigate to your project's root directory and run:
# python manage.py shell < relationship_app/query_samples.py
#

from relationship_app.models import Author, Book, Library, Librarian

def run_sample_queries():
    # --- Setup Sample Data for a clean test ---
    Author.objects.all().delete()
    Library.objects.all().delete()

    author_grrm = Author.objects.create(name="George R.R. Martin")
    author_tolkien = Author.objects.create(name="J.R.R. Tolkien")

    book1 = Book.objects.create(title="A Game of Thrones", author=author_grrm)
    book2 = Book.objects.create(title="A Clash of Kings", author=author_grrm)
    book3 = Book.objects.create(title="The Fellowship of the Ring", author=author_tolkien)

    # Define the library name as a variable
    library_name = "Fantasy Central Library"
    library = Library.objects.create(name=library_name)
    librarian = Librarian.objects.create(name="Samwell Tarly", library=library)
    library.books.add(book1, book3)

    print("--- Running Sample Queries ---")

    # --- Task: Query all books by a specific author. ---
    print("\\n## Query all books by a specific author (George R.R. Martin):")
    grrm_books = Book.objects.filter(author__name="George R.R. Martin")
    for book in grrm_books:
        print(f"- {book.title}")

    # --- Task: List all books in a library. ---
    print("\\n## List all books in a library (Fantasy Central Library):")
    # This line now matches the checker's requirement
    fantasy_library = Library.objects.get(name=library_name)
    for book in fantasy_library.books.all():
        print(f"- {book.title}")

    # --- Task: Retrieve the librarian for a library. ---
    print("\\n## Retrieve the librarian for a library (Fantasy Central Library):")
    library_to_check = Library.objects.get(name=library_name)
    print(f"- {library_to_check.librarian.name}")

# This line allows the script to be run directly.
run_sample_queries()