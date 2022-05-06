from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class BoulangerieSubDepartmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'sub_department',]
    list_display_links = ['id','sub_department', ]
    list_per_page =30

class BoulangerieProductsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'product', 'category', 'sub_department',]
    list_display_links = ['id','product', 'category', 'sub_department', ]
    list_per_page =30

class SessionsAdmin(ImportExportModelAdmin):
    list_display = ['id',  'session',]


class BoulangerieInventoryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'session', 'department', 'sub_department','stock_status','employee',
    'product', 'qty', 'unit_cost_price', 'unit_selling_price', 'total_cost_price', 'total_selling_price',]
    search_fields = [ 'product__accounts_dr', 'product__accounts_cr',]
    list_display_links = ['id', 'created_at', 'department', ]
    list_per_page =30
    list_filter = ('department', 'session', 'department','employee',)
    list_editable = ('product', 'qty', 'unit_cost_price', 'unit_selling_price', )

class BoulangeriePurchasesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'session', 'department', 'sub_department','employee', 'stock_status',
    'product', 'qty', 'unit_cost_price', 'unit_selling_price', 'total_cost_price', 'total_selling_price',]
    search_fields = [ 'product__accounts_dr', 'product__accounts_cr',]
    list_display_links = ['id', 'created_at', 'department', ]
    list_per_page =30
    list_filter = ('department', 'session', 'department','employee',)
    list_editable = ('product', 'qty', 'unit_cost_price', 'unit_selling_price', )

class BoulangerieReturnsDamagesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'session', 'department','employee',  'sub_department',
    'product', 'qty', 'unit_cost_price', 'unit_selling_price', 'total_cost_price', 'total_selling_price',]
    search_fields = [ 'product__accounts_dr', 'product__accounts_cr',]
    list_display_links = ['id', 'created_at', 'department', ]
    list_per_page =30
    list_filter = ('department', 'session', 'department','employee',)
    list_editable = ('product', 'qty', 'unit_cost_price', 'unit_selling_price', )


class BoulangerieLedgerAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'session', 'department','employee',
    'description', 'amount', 'accounts_dr', 'accounts_cr',]
    search_fields = [ 'product__accounts_dr', 'product__accounts_cr',]
    list_display_links = ['id', 'created_at', 'department', ]
    list_per_page =30
    list_filter = ('department', 'session', 'department','employee',)
    list_editable = ( 'amount', 'accounts_dr', 'accounts_cr', )


admin.site.register(BoulangerieSubDepartment, BoulangerieSubDepartmentAdmin)
admin.site.register(BoulangerieProducts, BoulangerieProductsAdmin)
admin.site.register(Sessions, SessionsAdmin)
admin.site.register(BoulangerieReturnsDamages, BoulangerieReturnsDamagesAdmin)
admin.site.register(BoulangerieLedger, BoulangerieLedgerAdmin)
admin.site.register(BoulangeriePurchases, BoulangeriePurchasesAdmin)
admin.site.register(BoulangerieInventory, BoulangerieInventoryAdmin)
