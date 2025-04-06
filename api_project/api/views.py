from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet("viewsets.ModelViewSet"):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

