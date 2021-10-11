from .models import Author, Book, Genre
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import AuthorSerializer, BookSerializers, GenreSerializer
from django_filters import rest_framework as filters
from .filters import BookFilter

class BookSetRest(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    filter_backends = [filters.DjangoFilterBackend, ]
    filterset_class = BookFilter
    


class AuthorSetRest(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreSetRest(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer