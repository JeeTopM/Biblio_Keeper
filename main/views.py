from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h4>Главная страница с информацией</h4>")

def readers(request):
    return HttpResponse("<h4>Тут будут отображены читатели и выданные/взятые ими книги</h4>")

def books(request):
    return HttpResponse("<h4>Тут будут отображены книги, которые нужно закупить и кто просил это сделать</h4>")
