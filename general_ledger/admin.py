from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class BankAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department','employee_management','transaction_id',
    'employee','amount', 'accounts_dr', 'accounts_cr',]
    search_fields = [ 'product__accounts_dr', 'product__accounts_cr',]
    list_display_links = ['id', 'created_at', 'transaction_id', 'department', ]
    list_per_page =30
    list_filter = ('department','employee_management','bank_name', 'accounts_dr', 'accounts_cr', )
    list_editable = ( 'amount', 'accounts_dr', 'accounts_cr', )

class CreditorsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department','employee_management','transaction_id', 'invoice_id',
    'employee', 'vendor','amount', 'accounts_dr', 'accounts_cr',]
    search_fields = [ 'product__accounts_dr', 'product__accounts_cr',]
    list_display_links = ['id', 'created_at', 'invoice_id', 'department', 'vendor', ]
    list_per_page =30
    list_filter = ('department','employee_management','vendor', 'accounts_dr', 'accounts_cr', )
    list_editable = ( 'amount', 'accounts_dr', 'accounts_cr', )


class PurchasesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department','employee_management','invoice_id',
    'employee', 'vendor','amount', 'accounts_dr', 'accounts_cr',]
    search_fields = [ 'product__accounts_dr', 'product__accounts_cr',]
    list_display_links = ['id', 'created_at', 'invoice_id', 'department', 'vendor', ]
    list_per_page =30
    list_filter = ('department','employee_management','vendor', 'accounts_dr', 'accounts_cr', )
    list_editable = ( 'amount', 'accounts_dr', 'accounts_cr', )

class AccountsPayableAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department','employee_management','transaction_id',
    'employee', 'institution','amount', 'accounts_dr', 'accounts_cr',]
    search_fields = [ 'product__accounts_dr', 'product__accounts_cr',]
    list_display_links = ['id', 'created_at', 'transaction_id', 'department', 'institution', ]
    list_per_page =30
    list_filter = ('department','employee_management','institution', 'accounts_dr', 'accounts_cr', )
    list_editable = ( 'amount', 'accounts_dr', 'accounts_cr', )

class ExpensesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created_at', 'department','employee_management','transaction_id',
    'employee', 'institution','amount', 'accounts_dr', 'accounts_cr',]
    search_fields = ['product__accounts_dr', 'product__accounts_cr',]
    list_display_links = ['id', 'created_at', 'transaction_id', 'department', 'institution', ]
    list_per_page =30
    list_filter = ('department','employee_management','institution', 'accounts_dr', 'accounts_cr', )
    list_editable = ( 'amount', 'accounts_dr', 'accounts_cr', )

admin.site.register(Bank, BankAdmin)
admin.site.register(Creditors, CreditorsAdmin)
admin.site.register(Purchases, PurchasesAdmin)
admin.site.register(AccountsPayable, AccountsPayableAdmin)
admin.site.register(Expenses, ExpensesAdmin)
