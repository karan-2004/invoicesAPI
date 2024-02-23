from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        exclude = ['invoice','id']
        read_only_fields = ['price']


class InvoiceSerializer(serializers.ModelSerializer):
    invoiceDetails = serializers.StringRelatedField(many = True)
    class Meta:
        model = Invoice
        exclude = ['id']





