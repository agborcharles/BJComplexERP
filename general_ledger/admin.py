from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class GeneralLedgerAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department','employee_management','transaction_id',
    'reference_id', 'institution','amount', 'accounts_dr', 'accounts_cr',]
    search_fields = ['supplier__institution', 'product__accounts_dr', 'product__accounts_cr',]
    list_display_links = ['id', 'created_at', 'transaction_id',
    'reference_id', 'institution', ]
    list_per_page =30
    list_filter = ('department','employee_management','institution', 'accounts_dr', 'accounts_cr', )
    list_editable = ( 'amount', 'accounts_dr', 'accounts_cr', )
admin.site.register(GeneralLedger, GeneralLedgerAdmin)
