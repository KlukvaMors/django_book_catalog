from typing import Any

from django.db import models
from django.db.models import query
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

import markdown

from book_catalog.filters import BookFilter
from .models import PERM_CAN_EDIT, Author, Book

def index(request):
    with open("README.md") as f:
        readme = f.read()
    readme = markdown.markdown(readme)
    return render(request, 'index.html', {'readme': readme})


# === Book Views ===

class BookListView(generic.ListView):
    model = Book
    template_name = 'book/list.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = BookFilter(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = BookFilter(self.request.GET, queryset)
        context['filter'] = filter
        return context

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book/detail.html'

class BookCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Book
    template_name = 'book/form.html'
    permission_required = f'book_catalog.{PERM_CAN_EDIT[0]}'
    fields = ['title', 'summary', 'date_of_release', 'image']

class BookUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Book
    template_name = 'book/form.html'
    permission_required = f'book_catalog.{PERM_CAN_EDIT[0]}'
    fields = ['title', 'summary', 'date_of_release', 'image']

class BookDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Book
    template_name = 'book/confirm_delete.html'
    permission_required = f'book_catalog.{PERM_CAN_EDIT[0]}'
    success_url = reverse_lazy('book-list')


# === Author Views ===

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author/list.html'
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author/detail.html'

class AuthorCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Author
    template_name = 'author/form.html'
    permission_required = f'book_catalog.{PERM_CAN_EDIT[0]}'
    fields = ['full_name', 'date_of_birth', 'image']

class AuthorUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Author
    template_name = 'author/form.html'
    permission_required = f'book_catalog.{PERM_CAN_EDIT[0]}'
    fields = ['full_name', 'date_of_birth', 'image']

class AuthorDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Author
    template_name = 'author/confirm_delete.html'
    permission_required = f'book_catalog.{PERM_CAN_EDIT[0]}'
    success_url = reverse_lazy('author-list')
