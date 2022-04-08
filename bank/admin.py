from django.contrib import admin
from . models import *

from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin

from django.apps import apps
from django.db import models
# Register your models here.

'''
class BankChargesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'bank_account',  'transaction_id',
                    'amount', 'account_dr', 'account_cr',]


class WithdrawalAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'bank_account', 'department', 'transaction_id',
                    'amount', 'account_dr', 'account_cr', 'reciept1', 'reciept2']

class DepositAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'bank_account', 'department', 'transaction_id',
                    'amount', 'account_dr', 'account_cr', 'reciept1', 'reciept2']

class ManagersAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'name', ]

class BankAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'name', 'city', 'location', 'phone1', 'phone2', 'email']

class BankAccountAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'bank_name', 'account_number', 'account_holder_name',
                    'account_type', 'is_active', 'account_balance',]

class BankOpeningBalAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'bank_account', 'amount', 'account_dr', 'account_cr',]

admin.site.register(Bank, BankAdmin)
admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(Managers, ManagersAdmin)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(Withdrawal, WithdrawalAdmin)
admin.site.register(BankCharges, BankChargesAdmin)
admin.site.register(BankOpeningBal, BankOpeningBalAdmin)
'''
