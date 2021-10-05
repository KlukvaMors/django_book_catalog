from django.db import models
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from book_catalog.filters import BookFilter
from .models import Author, Book

def index(request):
    return render(request, 'index.html')


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'

def book_list(request):
    filter = BookFilter(request.GET, queryset=Book.objects.all())
    return render(request, 'book_list.html', {'filter': filter})


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'

class AuthorCreateView(generic.CreateView):
    model = Author
    template_name = 'author_form.html'
    fields = ['full_name', 'date_of_birth', 'image']

class AuthorUpdateView(generic.UpdateView):
    model = Author
    template_name = 'author_form.html'
    fields = ['full_name', 'date_of_birth', 'image']

class AuthorDeleteView(generic.DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('index')
