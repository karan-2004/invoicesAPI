from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailsSerializer
from rest_framework.permissions import AllowAny

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    lookup_field = 'customerName'
    permission_classes = [AllowAny]

class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailsSerializer
    lookup_field = 'description'

    
    def get_invoice(self):
        # Get the invoice ID from the URL parameters
        invoice_id = self.kwargs.get('nested_1_customerName')
        try:
            return Invoice.objects.get(customerName=invoice_id)
        except Invoice.DoesNotExist:
            return None

    def get_queryset(self):
        invoice = self.get_invoice()
        return InvoiceDetail.objects.filter(invoice=invoice)
    

    def create(self, request, *args, **kwargs):
        invoice = self.get_invoice()
        if not invoice:
            return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)

        # Set the invoice for the new detail
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(invoice=invoice)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        invoice = self.get_invoice()
        if not invoice:
            return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update the detail by primary key
        partial = kwargs.pop('partial', False)
        detail = self.get_object()
        serializer = self.get_serializer(detail, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_updates(self, request, *args, **kwargs):
        invoice = self.get_invoice()
        if not invoice:
            return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)

        # Partial update logic
        partial = True
        detail = self.get_object()
        serializer = self.get_serializer(detail, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        invoice = self.get_invoice()
        if not invoice:
            return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)

        # Delete the detail by primary key
        detail = self.get_object()
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)