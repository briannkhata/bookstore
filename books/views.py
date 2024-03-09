from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'books':
                {
                    "title": "Web Development with Django - Second Edition: A definitive guide to building modern Python web applications using Django 4",
                    "thumbnailUrl": "",
                 }
               }
    return render(request, 'books/index.html', context)
