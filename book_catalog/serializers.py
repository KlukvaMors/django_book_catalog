from django.db import models
from rest_framework import serializers
from .models import Book, Author, Genre

class BookSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'summary', 'date_of_release', 'image')


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ['full_name', 'date_of_birth', 'image']


class GenreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Genre
        fields = ['name', ]