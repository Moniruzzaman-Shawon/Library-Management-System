from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from books.models import Book, Author, Category
from members.models import Member
from borrow.models import BorrowRecord
from .serializers import (AuthorSerializer, CategorySerializer, BookSerializer,
                          MemberSerializer, BorrowRecordSerializer)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        borrow_record = self.get_object()
        if borrow_record.is_returned:
            return Response({'detail': 'Book already returned'}, status=status.HTTP_400_BAD_REQUEST)
        borrow_record.is_returned = True
        borrow_record.return_date = timezone.now()
        borrow_record.save()

        book = borrow_record.book
        book.availability_status = True
        book.save()

        return Response({'detail': 'Book returned successfully'})
