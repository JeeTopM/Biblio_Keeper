from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("readers", views.readers, name="readers"),
    path("books", views.books, name="books"),
]
