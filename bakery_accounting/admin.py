from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class BakeryRmReturnsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department','return_manager','supplier',
    'return_id', 'product','qty', 'unit_cost_price', 'total_cost_price',]
    search_fields = ['supplier__startswith', 'product__startswith', ]
    list_display_links = ['id', 'created_at', 'product' ]
    list_per_page =200
    list_filter = ('created_at', 'supplier', 'product' )
    list_editable = ( 'qty', 'unit_cost_price', )

class BakeryRmDamagesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at',  'department','damage_id', 'product','qty',
    'unit_cost_price', 'total_cost_price',]
    search_fields = ['product__startswith', ]
    list_display_links = ['id', 'created_at', 'product' ]
    list_per_page =200
    list_filter = ('created_at', 'product', )
    list_editable = ( 'qty', 'unit_cost_price', )


class BakeryPurchaseAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department','procuement_manager','supplier',
    'purchase_id', 'product','qty', 'unit_cost_price', 'total_cost_price',]
    search_fields = ['supplier__startswith', 'product__startswith', ]
    list_display_links = ['id', 'created_at', 'product' ]
    list_per_page =200
    list_filter = ('created_at', 'supplier', 'product' )
    list_editable = ( 'qty', 'unit_cost_price', )

class BakeryInventoryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at','department','sub_department','stock_status',
    'entry_measure', 'product','qty', 'unit_cost_price', 'total_cost_price',]
    search_fields = ['customer_from__startswith', 'product__startswith', ]
    list_display_links = ['id', 'created_at', 'sub_department','stock_status', 'product' ]
    list_per_page =200
    list_filter = ('created_at', 'sub_department','stock_status', 'product' )
    list_editable = ( 'qty', 'unit_cost_price', )


class BakeryReturnAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at','invoice_id','customer_from','return_id','customer_to',
    'department', 'sub_department','category', 'product', 'qty', 'cost_price', 'total_amount', ]
    search_fields = ['customer_from__startswith', 'product__startswith', ]
    list_display_links = ['id', 'created_at','customer_from','customer_to', 'department', 'sub_department',
    'category', 'product']
    list_per_page =200
    list_filter = ('created_at', 'department', 'customer_from','customer_from','department', 'sub_department','category', 'product')
    list_editable = ( 'invoice_id', 'return_id',)


class BakeryOpeningBalancesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at','openingbalance_id','department','customer',
     'total_amount',
    ]
    search_fields = ['customer__startswith', ]
    list_display_links = ['id', 'created_at', 'customer', 'department',]
    list_per_page =200
    list_filter = ('created_at', 'department', 'customer',)
    list_editable = ('total_amount',)


class BakeryPaymentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at','collector','payment_id', 'session','customer',
    'department', 'amount',
    ]
    search_fields = ['customer__startswith', 'collector__startswith',]
    list_display_links = ['id', 'created_at', 'customer', 'department',]
    list_per_page =200
    list_filter = ('created_at', 'department','customer',)
    list_editable = ( 'payment_id', 'amount')



class BakerySalesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at','invoice_id','supplier','customer',
    'session', 'category', 'product', 'qty', 'cost_price', 'total_amount', 'discount',
    'discount_value', 'net_amount', 'commission']
    search_fields = ['customer__startswith', 'product__startswith', 'supplier__startswith']
    list_display_links = ['id', 'created_at', 'supplier','customer', 'category', 'product']
    list_per_page =100
    list_filter = ('created_at', 'department', 'supplier','customer',
    'category', 'product')
    list_editable = ( 'invoice_id',)


admin.site.register(BakeryReturn, BakeryReturnAdmin)
admin.site.register(BakeryOpeningBalances, BakeryOpeningBalancesAdmin)
admin.site.register(BakeryPayment, BakeryPaymentAdmin)

admin.site.register(BakerySales, BakerySalesAdmin)
admin.site.register(BakeryInventory, BakeryInventoryAdmin)
admin.site.register(BakeryPurchase, BakeryPurchaseAdmin)
admin.site.register(BakeryRmDamages, BakeryRmDamagesAdmin)
admin.site.register(BakeryRmReturns, BakeryRmReturnsAdmin)
