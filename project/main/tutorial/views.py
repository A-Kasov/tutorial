from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'tutorial/index.html')


def test(request):
    return render(request, 'tutorial/test.html')


def about(request):
    return render(request, 'tutorial/about.html')


def create(request):
    return render(request, 'tutorial/create.html')
