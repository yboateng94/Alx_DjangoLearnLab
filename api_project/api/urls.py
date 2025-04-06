from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (optional, if you want to retain the previous list view)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for CRUD operations
    path('', include(router.urls)),
]