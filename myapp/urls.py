from django.urls import path
from .views import InvoiceListCreateView, InvoiceRetrieveUpdateDestroyView

urlpatterns = [
    path('invoices/', InvoiceListCreateView.as_view()),
    path('invoices/<pk>/', InvoiceRetrieveUpdateDestroyView.as_view()),
]

