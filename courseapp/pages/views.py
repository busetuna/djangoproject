from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def iletisim(request):
    return render(request, 'pages/contact.html')

def hakkimizda(request):
    return render(request, 'pages/about.html')