from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'tutorial/index.html')


def test(request):
    return HttpResponse("Тестовая страница")
