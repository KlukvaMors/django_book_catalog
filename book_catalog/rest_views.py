from .models import Author, Book, Genre
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import AuthorSerializer, BookSerializers, GenreSerializer


class BookSetRest(viewsets.ModelViewSet, IsAuthenticated):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class AuthorSetRest(viewsets.ModelViewSet, IsAuthenticated):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreSetRest(viewsets.ModelViewSet, IsAuthenticated):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer