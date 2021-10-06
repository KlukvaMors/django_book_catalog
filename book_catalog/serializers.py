from django.db import models
from rest_framework import serializers
from .models import Book, Author, Genre

class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'summary', 'date_of_release', 'image', 'author')


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'full_name', 'date_of_birth', 'image']


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']