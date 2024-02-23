from typing import Iterable
from django.db import models

class Invoice(models.Model):
    date = models.DateField(auto_now_add = True)
    customerName = models.CharField(max_length = 200)


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name = 'invoiceDetails', on_delete = models.CASCADE)
    description = models.TextField()
    unitPrice = models.IntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField()

    def save(self, *args, **kwargs):
        self.price = self.unitPrice*self.quantity
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        arr = self.description.split()
        return " ".join(arr[:2])