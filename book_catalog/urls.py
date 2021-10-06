"""django_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('books/', views.BookListView.as_view(), name='book-list'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/create', views.BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/update', views.BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete', views.BookDeleteView.as_view(), name='book-delete'),

    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author/create', views.AuthorCreateView.as_view(), name='author-create'),
    path('author/<int:pk>/update', views.AuthorUpdateView.as_view(), name='author-update'),
    path('author/<int:pk>/delete', views.AuthorDeleteView.as_view(), name='author-delete'),
]
