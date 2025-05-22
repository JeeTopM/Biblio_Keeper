from django.urls import path
from . import views

urlpatterns = [
    path("", views.readers_home, name="readers_home"),
    path("create_readers", views.create_readers, name="create_readers"),
    path("<int:pk>", views.ReadersDetailView.as_view(), name="readers-detail"),
    path("<int:pk>/update", views.ReadersUpdateView.as_view(), name="readers-update"),
    path("<int:pk>/delete", views.ReadersDeleteView.as_view(), name="readers-delete"),
]
