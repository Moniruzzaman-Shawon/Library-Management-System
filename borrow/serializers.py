from rest_framework import serializers
from borrow.models import BorrowRecord
from books.models import Book          
from members.models import Member        
from library.serializers import BookSerializer
from library.serializers import MemberSerializer

class BorrowRecordSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.filter(availability_status=True), 
        source='book', 
        write_only=True
    )

    member = MemberSerializer(read_only=True)
    member_id = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(), 
        source='member', 
        write_only=True
    )

    class Meta:
        model = BorrowRecord
        fields = ['id', 'book', 'book_id', 'member', 'member_id', 'borrow_date', 'return_date', 'is_returned']
