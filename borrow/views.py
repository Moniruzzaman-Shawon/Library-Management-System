from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from borrow.models import BorrowRecord
from .serializers import BorrowRecordSerializer
from books.models import Book

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

    # Override create to update Book availability when borrowed
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.validated_data['book']
        if not book.availability_status:
            return Response({"error": "Book is not available for borrowing."}, status=status.HTTP_400_BAD_REQUEST)

        # Mark book unavailable
        book.availability_status = False
        book.save()

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Custom action to return book
    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        borrow_record = self.get_object()
        if borrow_record.is_returned:
            return Response({'detail': 'Book already returned'}, status=status.HTTP_400_BAD_REQUEST)

        borrow_record.is_returned = True
        borrow_record.return_date = timezone.now()
        borrow_record.save()

        # Mark book available again
        book = borrow_record.book
        book.availability_status = True
        book.save()

        return Response({'detail': 'Book returned successfully'})
