from rest_framework import viewsets
from .models import Author, Category, Book
from .serializers import AuthorSerializer, CategorySerializer, BookSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsLibrarian



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    list:
    View all books.

    retrieve:
    View a single book.

    create/update/destroy:
    Only librarians can perform these actions.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsLibrarian]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]