from django.contrib import admin
from .models import Invoice, InvoiceDetail

class InvoiceDetailAdmin(admin.StackedInline):
    model = InvoiceDetail
    extra = 0

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceDetailAdmin]

admin.site.register(Invoice, InvoiceAdmin)