from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    return render(request, 'index.html')

def books(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, 'add_book.html', context)

def authors(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, 'add_author.html', context) 


def add_book(request):

    title = request.POST['title']
    desc = request.POST['desc']
    Book.objects.create(title=title, desc=desc)

    return redirect('/books')

def book_info(request, book_id):
    context = {
        "book": Book.objects.get(id=book_id),
        "authors": Author.objects.exclude(books__id=book_id)
    }
    return render(request, 'book_info.html', context)


def assign_book(request, book_id):

    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)

    return redirect(f'/books/{book_id}')



def add_author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)

    return redirect('/authors')

def author_info(request, author_id):
    context = {
        'author': Author.objects.get(id=author_id),
        'books': Book.objects.exclude(authors__id=author_id)
    }
    return render(request, 'author_info.html', context)


def assign_author(request, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)

    return redirect(f'/authors/{author_id}')
