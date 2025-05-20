from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "main/index.html")


def readers(request):
    return render(request, "main/readers.html")


def books(request):
    return render(request, "main/books.html")
