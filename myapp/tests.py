# myapp/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(APITestCase):
    def test_create_invoice(self):
        data = {'date': '2024-01-10', 'customer_name': 'Test Customer'}
        response = self.client.post('/invoices/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Add more test cases for other CRUD operations and edge cases