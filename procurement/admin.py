from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class ProcurementAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department','procurement_manager','vendor',
    'amount']
    #search_fields = ['supplier__institution', 'product__accounts_dr', 'product__accounts_cr',]
    list_display_links = ['created_at', 'department','procurement_manager','vendor']
    list_per_page =30
    #list_filter = ('department','employee_management','institution', 'accounts_dr', 'accounts_cr', )
    #list_editable = ( 'amount', 'accounts_dr', 'accounts_cr', )
admin.site.register(Procurement, ProcurementAdmin)
