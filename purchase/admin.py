from django.contrib import admin
from . models import *

from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

from django.apps import apps
from django.db import models
import tablib
import collections


class PurchaseAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created' ,'vendor', 'invoice_id','amount',
    'stock_dept_invoice_id', 'vat_amount' , 'grand_total','due_date',]

    editable = ['created', 'vendor', 'description','amount', 'due_date', ]
    list_filter = ('vendor',)
    # search list
    search_fields = ('vendor', )
    list_display_links = ['id', 'vendor', 'invoice_id','amount',]



class VendorAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'vendor_name', 'vendor_type', 'phone', 'residential_city', 'residential_address',
                    'slug']

class OpeningBalanceAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'vendor', 'amount' ]


class OrderItemAdmin(ImportExportModelAdmin):
    list_display = ['id', 'purchase_order', 'product', 'qty', 'price', 'discount_price',
                        'final_price', 'total_price']

    list_editable = ('qty','price',)
    search_fields = ['purchase_order__startswith', ]
    list_display_links = ['id', 'purchase_order', 'product' ]

class PaymentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'invoice_id', 'installment', 'invoice_number',
            'invoice_amount', 'payment_id', 'amount_paid', 'balance_due', 'status',]



admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(OpeningBalance, OpeningBalanceAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Payment, PaymentAdmin)




'''
class OpeningReturnAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created',  'employee', 'vendor', 'description','invoice_number', 'return_id', 'vendor', 'amount'
                        , ]

class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'name']


class ProductAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'name', 'category' ]



admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(OpeningReturn, OpeningReturnAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
'''
