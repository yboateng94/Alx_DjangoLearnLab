import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = ["Author.objects.get(name=author_name)"]
    if author:
        return Book.objects.filter(author=author)
    return []

# List all books in a library
def get_books_in_library(library_name):
    library = ["Library.objects.get(name=library_name)"]
    if library:
        return library.books.all()
    return []

# Retrieve the librarian for a library
def get_librarian_of_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        return Librarian.objects.filter(library=library).first()
    return None

# Example usage
if __name__ == "__main__":
    print(get_books_by_author("J.K. Rowling"))
    print(get_books_in_library("City Library"))
    print(get_librarian_of_library("City Library"))
