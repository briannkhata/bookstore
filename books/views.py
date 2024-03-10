from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from books.models import Book


def index(request):
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request, 'books/index.html', context)


def show(request, id):
    try:
        singleBook = get_object_or_404(Book, pk=id)
    except Book.DoesNotExist:
        return Http404('Book not Found')
    context = {'book': singleBook}
    return render(request, 'books/show.html', context)
