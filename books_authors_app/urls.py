
from django.urls import path
from . import views

urlpatterns = [
  path('',views.index),
  path('create_books', views.create_books),
  path('books/<book_id>', views.books, name="books"),
  path('authors', views.authors),
  path('create_authors', views.create_authors),
  path('author/<author_id>', views.author, name="author"),
  path('select_book', views.select_book, name="select_book"),
  path('add_book', views.add_book)
]
