from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet


from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer, BookSerializer2


class BookViewSet(ModelViewSet):
    #queryset = Book.objects.all()
    queryset = Book.objects.filter(is_online=True)
    serializer_class = BookSerializer
    permission_classes = []

    @action(['get'], False, 'all', 'all')
    def all_books(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

@api_view(['put'])
def update_book(request):
    s = BookSerializer2(data=request.data)
    s.is_valid(raise_exception=True)
    Book.objects.filter(pk=1).update(**s.validated_data)

    return Response(BookSerializer(Book.objects.first()).data)
