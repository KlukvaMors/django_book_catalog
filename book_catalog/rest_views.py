from .models import Author, Book, Genre
from rest_framework import viewsets
from .serializers import AuthorSerializer, BookSerializers, GenreSerializer


class BookSetRest(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class AuthorSetRest(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreSetRest(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer