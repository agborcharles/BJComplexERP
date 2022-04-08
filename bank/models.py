from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from bank.utils import create_new_ref_number
from django.core.validators import RegexValidator, MinValueValidator
from django.db.models.signals import post_save
from decimal import Decimal

import datetime
from configurations.models import *

from django.db.models import F, Sum, Value
from django.db.models.functions import Coalesce


# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    phone1 = models.CharField(max_length=255, blank=True, null=True)
    phone2 = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.name

    class Meta():
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'
        ordering: ['created_at']

class BankAccount(models.Model):
    ACCOUNT_TYPE = (
        ('Current', 'Current'),
        ('Savings', 'Savings'),
        ('Blocked', 'Blocked'),
        ('Joint', 'Joint'),
        ('Loan', 'Loan'),
    )
    created = models.DateTimeField(auto_now_add=True)
    bank_name =  models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='bank',)
    account_number = models.CharField(max_length=255)
    #account_holder_name = models.ForeignKey(Worker, null=True, on_delete=models.SET_NULL, blank = True,)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE, default='Current Account')
    is_active = models.BooleanField(default=True)

    slug = models.SlugField(max_length=100, unique=True, blank=True)

    account_balance = models.IntegerField(default=0, null = True, blank = True)

    bank_documents1 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    bank_documents2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    bank_documents3 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    bank_documents4 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    bank_documents5 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    bank_documents6= models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.account_number

    def save(self, *args, **kwargs):
        self.slug = slugify(self.account_number)
        super(BankAccount, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('bank:account-detail', args=[self.slug])

    class Meta():
        verbose_name = 'BankAccounts'
        verbose_name_plural = 'BankAccounts'
        ordering: ['created_at']


class Managers(models.Model):
    name = models.CharField(max_length=90)
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'


def increment_invoice_number():
    last_invoice = Deposit.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice:
         return today_string + "-" + 'BNKDINV0001'

    transaction_id = last_invoice.transaction_id
    invoice_int = int(transaction_id.split('BNKDINV000')[-1])
    new_invoice_int = invoice_int + 1

    new_transaction_id = today_string + "-" + 'BNKDINV000'  + str(new_invoice_int)
    return new_transaction_id



class BankOpeningBal(models.Model):
    created = models.DateField("Date", default=now)
    bank_account = models.ForeignKey(BankAccount, null=True, on_delete=models.SET_NULL, blank = True)
    description = models.TextField(max_length=200, default='Bank Opening Balance')
    amount = models.IntegerField(null = True, blank = True, default=0,)
    #account_dr = models.ForeignKey(AccountsDebit,  null=True, on_delete=models.SET_NULL, default=6)
    #account_cr = models.ForeignKey(AccountsCredit,  null=True, on_delete=models.SET_NULL, default=1)


    def __str__(self):
        return self.description

    class Meta():
        verbose_name = 'Bank Opening Bal'
        verbose_name_plural = 'Bank Opening Bal'
        ordering: ['created']

def bank_opening_bal(sender, **kwargs):
    if kwargs['created']:
        opening_bal_trans = BankOpeningBal.objects.create(bank_account=kwargs['instance'])

post_save.connect(bank_opening_bal, sender=BankAccount)



class Deposit(models.Model):

    created = models.DateField("Date", default=now)
    bank_account = models.ForeignKey(BankAccount, null=True, on_delete=models.SET_NULL, blank = True)
    #department =  models.ForeignKey(Department, null=True, on_delete=models.SET_NULL, blank = True, default=1 )
    transaction_id = models.CharField(max_length = 500, editable=False, default=increment_invoice_number, null = True, blank = True)
    description = models.TextField(max_length=200, default='Deposit')
    amount = models.IntegerField(null = True, blank = True, default=0,)
    #account_dr = models.ForeignKey(AccountsDebit,  null=True, on_delete=models.SET_NULL, default=6)
    #account_cr = models.ForeignKey(AccountsCredit,  null=True, on_delete=models.SET_NULL, default=1)
    reciept1 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    reciept2 = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta():
        verbose_name = 'Deposit'
        verbose_name_plural = 'Deposits'
        ordering: ['created']

def bank_deposit(sender, **kwargs):
    if kwargs['created']:
        deposit_trans = Deposit.objects.create(bank_account=kwargs['instance'])

post_save.connect(bank_deposit, sender=BankAccount)


def increment_invoice_number():
    last_invoice = Withdrawal.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice:
         return today_string + "-" + 'BNKWINV0001'

    transaction_id = last_invoice.transaction_id
    invoice_int = int(transaction_id.split('BNKWINV000')[-1])
    new_invoice_int = invoice_int + 1

    new_transaction_id = today_string + "-" + 'BNKWINV000'  + str(new_invoice_int)
    return new_transaction_id

class Withdrawal(models.Model):
    created= models.DateField("Date", default=now)
    bank_account = models.ForeignKey(BankAccount, null=True, on_delete=models.SET_NULL, blank = True)
    #department =  models.ForeignKey(Department, null=True, on_delete=models.SET_NULL, blank = True, default=1 )
    transaction_id = models.CharField(max_length = 500, editable=False, default=increment_invoice_number, null = True, blank = True)
    description = models.TextField(max_length=200, default='Withdrawal')
    amount = models.IntegerField(null = True, blank = True, default=0,)
    #account_dr = models.ForeignKey(AccountsDebit,  null=True, on_delete=models.SET_NULL, default=6)
    #account_cr = models.ForeignKey(AccountsCredit,  null=True, on_delete=models.SET_NULL, default=1)
    reciept1 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    reciept2 = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta():
        verbose_name = 'Withdrawal'
        verbose_name_plural = 'Withdrawals'
        ordering: ['created']

def bank_withdrawals(sender, **kwargs):
    if kwargs['created']:
        withdrawals_trans = Withdrawal.objects.create(bank_account=kwargs['instance'])

post_save.connect(bank_withdrawals, sender=BankAccount)

def increment_invoice_number():
    last_invoice = BankCharges.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice:
         return today_string + "-" + 'BNKCINV0001'

    transaction_id = last_invoice.transaction_id
    invoice_int = int(transaction_id.split('BNKCINV000')[-1])
    new_invoice_int = invoice_int + 1

    new_transaction_id = today_string + "-" + 'BNKCINV000'  + str(new_invoice_int)
    return new_transaction_id

class BankCharges(models.Model):
    created= models.DateField("Date", default=now)
    bank_account = models.ForeignKey(BankAccount, null=True, on_delete=models.SET_NULL, blank = True)
    transaction_id = models.CharField(max_length = 500, editable=False, default=increment_invoice_number, null = True, blank = True)
    description = models.TextField(max_length=200, default='Bank Charges')
    amount = models.IntegerField(null = True, blank = True, default=0,)
    #account_dr = models.ForeignKey(AccountsDebit,  null=True, on_delete=models.SET_NULL, default=6)
    #account_cr = models.ForeignKey(AccountsCredit,  null=True, on_delete=models.SET_NULL, default=1)

    def __str__(self):
        return self.description

    class Meta():
        verbose_name = 'Bank Charge'
        verbose_name_plural = 'Bank Charges'
        ordering: ['created']

def bank_charges(sender, **kwargs):
    if kwargs['created']:
        charges_trans = BankCharges.objects.create(bank_account=kwargs['instance'])

post_save.connect(bank_charges, sender=BankAccount)
