from django.shortcuts import render
from django.http import HttpResponse
import json

booksData = open("books/books.json").read()
data = json.loads(booksData)


def index(request):
    context = {'books': data}
    return render(request, 'books/index.html', context)


def show(request, id):
    singleBook = list()
    for book in data:
        if book['id'] == id:
            singleBook = book

    context = {'book': singleBook}
    return render(request, 'books/show.html', context)
