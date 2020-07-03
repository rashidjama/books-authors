from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context = {
      'books': Book.objects.all(),
      'authors': Author.objects.all()
    }
    return render(request, 'index.html', context)
def create_books(request):
  book = Book.objects.create(title = request.POST['title'],
  desc = request.POST['des'],
  )
  return redirect('/')

def books(request, book_id):
  item = Book.objects.get(id=book_id)
  context = {
    'book': item,
    'books': Book.objects.all(),
    'authors': Author.objects.all()
  }
  request.session['book_id'] = book_id
  return render(request, "books.html", context)

def authors(request):
  context = {
    'authors': Author.objects.all(),
    'books': Book.objects.all()
  }
  return render(request, 'authors.html', context)

def create_authors(request):
  author_obj = Author.objects.create(
    first_name = request.POST['first'], last_name = request.POST['last'], notes = request.POST['notes']
  )
  return redirect('/authors')

def author(request, author_id):
  aut = Author.objects.get(id=author_id)
  context = {
    'single_author': aut,
    'books': Book.objects.all()
  }
  request.session['author_id'] =author_id
  return render(request, 'single_author.html', context)

def add_book(request):
  request.session['pk_id'] = request.POST['book']
  author_obj = Author.objects.get(id= request.session['author_id'])
  author_obj.books.add(request.session['pk_id'])
  return redirect('/authors')

def select_book(request):
  book_obj = Book.objects.get(id=  request.session['book_id'])
  request.session['author_id'] = request.POST['authors']
  book_obj.authors.add(request.session['author_id'])
  return redirect('/')