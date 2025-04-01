from django.shortcuts import render
from .models import Book  # Assuming Book model exists in your app

def list_books(request):
    books = Book.objects.all()  # Query all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})


["from django.views.generic.detail import DetailView"]
from .models import Library  # Assuming Library model exists in your app

class LibraryDetailView('DetailView'):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'