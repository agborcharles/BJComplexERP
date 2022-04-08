from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CustomerAdmin(ImportExportModelAdmin):
    list_display = [ 'id', 'created', 'customer_name', 'slug',
                    'customer_type', 'is_active', ]
    # search list
    search_fields = ['customer_name']

class InvoiceAdmin(ImportExportModelAdmin):
    list_display = [ 'id', 'created', 'sales_session', 'stock_manager','slug','invoice_id',
                    'customer', 'stock_dept_invoice_id', 'amount',]
    # search list
    search_fields = ['invoice_id__startswith', ]
    list_display_links = ['id', 'created', 'sales_session','invoice_id','customer',  ]

class CustomerOpeningBalanceAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'customer', 'amount' ]

class InvoiceItemAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'invoice_id', 'product', 'price', 'quantity', 'discount', 'total']
    search_fields = ['invoice_id__icontains', ]
    list_display_links = ['id', 'created', 'invoice_id', 'product', 'price', 'quantity', ]

class InvoicePaymentAdmin(ImportExportModelAdmin):
    list_display = ['id','created', 'payment_session', 'employee','payment_installment',  'payment_id','invoice', 'total_amount', 'amount_paid', ]

admin.site.register(InvoicePayment, InvoicePaymentAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
admin.site.register(CustomerOpeningBalance, CustomerOpeningBalanceAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
