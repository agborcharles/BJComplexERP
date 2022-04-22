from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class SupermarketProductsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'product', 'category', 'unit_cost_price', 'unit_selling_price',]

class SupermarketReturnsDamagesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department','session','sales_person',
    'product', 'qty','unit_cost_price', 'total_cost_price',]
    #search_fields = ['supplier__institution', 'product__accounts_dr', 'product__accounts_cr',]
    list_display_links = ['id',  'department','session','sales_person',
    'product', 'qty','unit_cost_price', 'total_cost_price',]
    #'reference_id', 'institution', ]
    #list_per_page =30
    #list_filter = ('department','employee_management','institution', 'accounts_dr', 'accounts_cr', )
    #list_editable = ( 'amount', 'accounts_dr', 'accounts_cr', )


class SupermarketSalesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department','session','sales_person',
    'product', 'qty','unit_cost_price', 'unit_selling_price', 'total_cost_price', 'total_selling_price']
    #search_fields = ['supplier__institution', 'product__accounts_dr', 'product__accounts_cr',]
    list_display_links = ['id',  'department','session','sales_person',
    'product', 'qty','unit_cost_price', 'unit_selling_price', 'total_cost_price', 'total_selling_price']
    #'reference_id', 'institution', ]
    #list_per_page =30
    #list_filter = ('department','employee_management','institution', 'accounts_dr', 'accounts_cr', )
    #list_editable = ( 'amount', 'accounts_dr', 'accounts_cr', )
admin.site.register(SupermarketProducts, SupermarketProductsAdmin)
admin.site.register(SupermarketReturnsDamages, SupermarketReturnsDamagesAdmin)
admin.site.register(SupermarketSales, SupermarketSalesAdmin)
