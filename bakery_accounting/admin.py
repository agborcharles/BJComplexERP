from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class RawMaterialsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'product', 'category', 'entry_measure', 'weight_pack', 'cost_price', 'packaging' ]
    list_display_links = ['id', 'product', 'category', 'entry_measure', 'weight_pack', 'cost_price' ]
    list_per_page =500

class QuarterAdmin(ImportExportModelAdmin):
    list_display = ['id', 'quarter_name', ]
    list_display_links = ['id', 'quarter_name', ]
    list_per_page =500

class BakeryCustomersAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'customer','busness_type','quarter',
    'street','phone_1','phone_2',  'address', 'road_street_location',]
    #search_fields = ['supplier__startswith', 'product__startswith', ]
    list_display_links = ['id', 'customer','busness_type','phone_1',]
    list_per_page =200
    #list_filter = ('created_at', 'supplier', 'product' )
    #list_editable = ( 'qty', 'unit_cost_price', )

class BakeryRmReturnsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department', 'return_status','return_manager','supplier',
    'return_id', 'product','qty', 'unit_cost_price', 'total_cost_price',]
    search_fields = ['supplier__startswith', 'product__startswith', ]
    list_display_links = ['id', 'created_at', 'product' ]
    list_per_page =200
    list_filter = ('created_at', 'supplier', 'product' )
    list_editable = ( 'qty', 'unit_cost_price', )

class BakeryRawMaterialUsageAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department', 'product','qty',
    'unit_cost_price', 'total_cost_price',]
    search_fields = ['product__startswith', ]
    list_display_links = ['id', 'created_at', 'product' ]
    list_per_page =200
    list_filter = ('created_at', 'product', )
    list_editable = ( 'qty', 'unit_cost_price', )


class BakeryPurchaseAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department', 'location', 'procuement_manager','supplier',
    'purchase_id','stock_status', 'product','qty', 'unit_cost_price', 'total_cost_price',]
    search_fields = ['supplier__startswith', 'product__startswith', ]
    list_display_links = ['id', 'created_at', 'product' ]
    list_per_page =200
    list_filter = ('created_at', 'supplier', 'product' )
    list_editable = ( 'qty', 'unit_cost_price', )
#--------------------------------------------------------------#
class BakeryMagazineDistributionAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department', 'sub_department', 'sub_department_manager','stock_manager',
    'product','qty', 'unit_cost_price', 'total_cost_price',]
    search_fields = ['supplier__startswith', 'product__startswith', ]
    list_display_links = ['id', 'created_at', 'product' ]
    list_per_page =200
    list_filter = ('created_at', 'stock_manager', 'product' )
    list_editable = ( 'qty', 'unit_cost_price', )

#--------------------------------------------------------------#
class BakeryInventoryMagazineAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at','department','sub_department','stock_status',
    'entry_measure', 'product','qty', 'unit_cost_price', 'total_cost_price',]
    search_fields = ['customer_from__startswith', 'product__startswith', ]
    list_display_links = ['id', 'created_at', 'sub_department','stock_status', 'product' ]
    list_per_page =200
    list_filter = ('created_at', 'sub_department','stock_status', 'product' )
    list_editable = ( 'qty', 'unit_cost_price', )

#--------------------------------------------------------------#
class BakeryInventorySubDepartmentsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at','department','sub_department',
    'supervisor','stock_status','entry_measure', 'product','qty',
    'rm_total_weight_grams', 'unit_cost_price', 'total_cost_price',]
    search_fields = ['customer_from__startswith', 'product__startswith', ]
    list_display_links = ['id', 'created_at', 'sub_department','stock_status',
    'product']
    list_per_page =200
    list_filter = ('created_at', 'sub_department','stock_status', 'product' )
    list_editable = ( 'qty', 'unit_cost_price', )
#--------------------------------------------------------------#

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
    list_display = ['id', 'created_at','department', 'quarter', 'street','collector','payment_id',
     'session','customer', 'amount', 'payment_mode', ]
    search_fields = ['customer__startswith', 'collector__startswith',]
    list_display_links = ['id', 'created_at', 'customer', 'department', 'payment_mode', ]
    list_per_page =200
    list_filter = ('created_at', 'department', 'payment_mode', )
    list_editable = ( 'payment_id', 'amount')



class BakerySalesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at','invoice_id','supplier','customer',
    'session', 'category', 'product', 'qty', 'cost_price', 'total_amount', 'discount',
    'discount_value', 'net_amount', 'commission']
    search_fields = ['customer__startswith', 'product__startswith', 'supplier__startswith']
    list_display_links = ['id', 'created_at', 'supplier','customer', 'category', 'product']
    list_per_page =300
    list_filter = ('created_at', 'department', 'supplier','customer',
    'category', 'product')
    list_editable = ( 'invoice_id',)

class BakeryInventoryMagazineAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at','department','sub_department','stock_status',
    'entry_measure', 'product','qty', 'unit_cost_price', 'total_cost_price',]
    search_fields = ['customer_from__startswith', 'product__startswith', ]
    list_display_links = ['id', 'created_at', 'sub_department','stock_status', 'product' ]
    list_per_page =200
    list_filter = ('created_at', 'sub_department','stock_status', 'product' )
    list_editable = ( 'qty', 'unit_cost_price', )

#--------------------------------------------------------------#
class BakeryRmUsageSubDepartmentsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at','department','sub_department',
    'supervisor', 'session', 'entry_measure', 'product','qty',
    'rm_total_weight_grams', 'unit_cost_price', 'total_cost_price',]
    search_fields = ['customer_from__startswith', 'product__startswith', ]
    list_display_links = ['id', 'created_at', 'sub_department', 'product']
    list_per_page =200
    list_filter = ('created_at', 'sub_department', 'product' )
    list_editable = ( 'qty', 'unit_cost_price', )



admin.site.register(RawMaterials, RawMaterialsAdmin)
admin.site.register(Quarter, QuarterAdmin)
admin.site.register(BakeryCustomers, BakeryCustomersAdmin)
admin.site.register(BakeryReturn, BakeryReturnAdmin)
admin.site.register(BakeryOpeningBalances, BakeryOpeningBalancesAdmin)
admin.site.register(BakeryPayment, BakeryPaymentAdmin)

admin.site.register(BakerySales, BakerySalesAdmin)
admin.site.register(BakeryInventorySubDepartments, BakeryInventorySubDepartmentsAdmin)
admin.site.register(BakeryInventoryMagazine, BakeryInventoryMagazineAdmin)
admin.site.register(BakeryPurchase, BakeryPurchaseAdmin)
admin.site.register(BakeryMagazineDistribution, BakeryMagazineDistributionAdmin)
#admin.site.register(BakeryRmDamages, BakeryRmDamagesAdmin)

admin.site.register(BakeryRmUsageSubDepartments, BakeryRmUsageSubDepartmentsAdmin)
