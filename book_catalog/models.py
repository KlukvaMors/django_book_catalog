from django.db import models
from django.urls import reverse

from django.utils.translation import gettext as _



class Genre(models.Model):
    """Model representing a book genre."""

    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        return self.name


class Author(models.Model):
    """Model representing an author."""

    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    image = models.ImageField()

    class Meta:
        ordering = ['full_name', ]

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.full_name}'


class Book(models.Model):
    """Model representing a book """

    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    date_of_release = models.DateField()
    image = models.ImageField()

    # FK
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])