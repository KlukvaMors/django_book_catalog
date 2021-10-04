from django.db import models
from django.shortcuts import render
from django.views import generic
from .models import Author, Book

def index(request):
    return render(request, 'index.html')


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'