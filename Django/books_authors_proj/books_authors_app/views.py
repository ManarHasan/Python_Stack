from django.shortcuts import render, redirect
from .models import Books, Authors


def books(request):
    books = Books.objects.all()
    context = {
        "books": books
    }
    return render(request, "books.html", context)


def add_books(request):
    if request.method == "POST":
        Books.objects.create(
            title=request.POST['title'], desc=request.POST['description'])
        return redirect("/")


def book_profile(request, id):
    book = Books.objects.get(id=id)
    authors = Authors.objects.all()
    book_authors = Authors.objects.exclude(
        books=book).values_list('first_name', 'last_name', 'id')
    print(book_authors)
    context = {
        "book": book,
        "book_authors": book_authors,
        "authors": authors
    }
    return render(request, "book_profile.html", context)


def add_author_to_book(request, id):
    book = Books.objects.get(id=id)
    author = Authors.objects.get(id=request.POST['author'])
    book.authors.add(author)
    return redirect("/")


def authors(request):
    authors = Authors.objects.all()
    context = {
        "authors": authors
    }
    return render(request, "authors.html", context)


def add_author(request):
    Authors.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    return redirect("/authors")


def author_profile(request, id):
    author = Authors.objects.get(id=id)
    books = Books.objects.all()
    author_books = Books.objects.exclude(
        authors=author).values_list('title', 'id')
    print(author_books)
    context = {
        "author": author,
        "author_books": author_books,
        "books": books
    }
    return render(request, "author_profile.html", context)


def add_book_to_author(request, id):
    author = Authors.objects.get(id=id)
    book = Books.objects.get(id=request.POST['book'])
    author.books.add(book)
    return redirect("/authors")
