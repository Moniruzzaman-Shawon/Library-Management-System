from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import BorrowRecord
from .serializers import BorrowRecordSerializer

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
