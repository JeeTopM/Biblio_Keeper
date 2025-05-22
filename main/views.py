from django.shortcuts import render


# Create your views here.
def index(request):
    data = {"title": "Главная страница"}
    return render(request, "main/index.html", data)

def books(request):
    data = {'title': 'Работа с читателем, запись'}
    return render(request, "main/books.html", data)
