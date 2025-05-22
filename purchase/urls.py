from django.urls import path
from . import views

urlpatterns = [
    path("", views.purchase_home, name="purchase_home"),
    path("create_purchase", views.create_purchase, name="create_purchase"),
    path("<int:pk>", views.PurchaseDetailView.as_view(), name="purchase-detail"),
    path("<int:pk>/update", views.PurchaseUpdateView.as_view(), name="purchase-update"),
    path("<int:pk>/delete", views.PurchaseDeleteView.as_view(), name="purchase-delete"),
    path('all-books/', views.all_books, name='all-books'),
]