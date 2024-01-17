
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice

class InvoiceTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2024-01-17', 'Invoice_customerName': 'Test Customer'}
        self.invoice = Invoice.objects.create(**self.invoice_data)

    def test_create_invoice(self):
        response = self.client.post(reverse('invoice-list-create'), data=self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)

    def test_get_invoice_list(self):
        response = self.client.get(reverse('invoice-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_invoice(self):
        response = self.client.get(reverse('invoice-retrieve-update-destroy', args=[self.invoice.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Invoice_customerName'], self.invoice_data['Invoice_customerName'])

