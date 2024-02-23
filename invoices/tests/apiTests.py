from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from invoices.models import Invoice, InvoiceDetail

class InvoiceDetailApiTests(APITestCase):
    def setUp(self) -> None:
        self.invoice = Invoice.objects.create(customerName='john')
        self.invoiceDetail = InvoiceDetail.objects.create(invoice=self.invoice,
                                                          description = 'lorem ipsum',
                                                          unitPrice = 10,
                                                          quantity = 3)
    def testListInvoices(self):
        url = reverse('invoice-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
