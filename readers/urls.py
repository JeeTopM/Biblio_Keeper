from django.urls import path
from . import views

urlpatterns = [
    path("", views.readers_home, name="readers_home"),
    path("create_readers", views.create_readers, name="create_readers"),
]
