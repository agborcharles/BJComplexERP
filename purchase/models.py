from __future__ import unicode_literals
from django.db import models

from decimal import Decimal

from django.urls import reverse

from django.core.validators import RegexValidator, MinValueValidator

import uuid

import datetime
from django.utils.timezone import now
from django.template.defaultfilters import slugify

from django.db.models.signals import post_save
from configurations.models import *

from django.db.models import Sum
from django.conf import settings
from django.urls import reverse
from django.dispatch import receiver
# phone validator using regular expressions
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message='Phone number invalid. Should start with example: +237'
)



class Vendor(models.Model):

    Vendor_TYPE = (
        ('Company', 'Company'),
        ('Enterprise', 'Enterprise'),
        ('Individual', 'Individual'),
    )
    '''General information fields'''
    created = models.DateTimeField(auto_now_add=True)
    vendor_name = models.CharField(max_length=200)
    vendor_type = models.CharField(max_length=10, choices=Vendor_TYPE)
    company_name = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    '''Contact details fields'''
    residential_address = models.TextField(max_length=255, null=True)
    residential_city = models.CharField(max_length=100, default='Kumba')
    residential_region = models.CharField(max_length=200, default='South West Region')
    phone = models.CharField(validators=[phone_regex], max_length=15, null=True)
    email = models.EmailField(blank=True, null=True)

    '''Bank Details'''
    bank_name1 = models.CharField(max_length=200, blank=True, null=True)
    bank_account_name1 = models.CharField(max_length=200, blank=True, null=True)
    bank_account_number1 = models.CharField(max_length = 30, blank=True, editable=True, unique=True, null=True )
    bank_name2 = models.CharField(max_length=200, blank=True, null=True)
    bank_account_name2 = models.CharField(max_length=200, blank=True, null=True)
    bank_account_number2 = models.CharField(max_length = 30, blank=True, editable=True, unique=True, null=True )


    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    def __str__(self):
        return self.vendor_name

    class Meta:
        verbose_name = 'vendor'
        verbose_name_plural = 'vendor'

    # def get_account_name(self):
    #     '''Make client's name the same as account name'''
    #     self.account_name = self.name
    #     return self.account_name
    def get_absolute_url(self):
        return reverse('purchase:vendor-details', args=[self.slug])

    def save(self, *args, **kwargs):
            self.slug = slugify(self.vendor_name)
            super(Vendor, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']


class OpeningBalance(models.Model):
    created = models.DateField(default=now)
    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.vendor)

    class Meta:
        ordering = ['-created']

# ---- OpeningBalance Signal ---- #
def opening_balance(sender, **kwargs):
    if kwargs['created']:
        opening_balance_trans = OpeningBalance.objects.create(vendor=kwargs['instance'])

post_save.connect(opening_balance, sender=Vendor)

# --------------- INVOICE NUMBER GENERATOR FOR Purhcases------------ #
def increment_invoice_number():
    last_invoice = Purchase.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice:
            return today_string + "-" + 'INV0001'

    invoice_id = last_invoice.invoice_id
    invoice_int = int(invoice_id.split('INV000')[-1])
    new_invoice_int = invoice_int + 1

    new_invoice_id = today_string + "-" + 'INV000'  + str(new_invoice_int)
    return new_invoice_id

class Purchase(models.Model):
    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
        ('Boulangerie', 'Boulangerie'),
        ('Supermarket', 'Supermarket'),
        ('Bar', 'Bar'),
        ('Snack', 'Snack'),
        ('Ice Cream', 'Ice Cream'),

    )
    created = models.DateField(default=now)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='', null = True, blank = True, verbose_name = 'Department')
    procurement_manager = models.CharField(max_length = 500, null = True, blank = True, verbose_name = "Procurement Manager")
    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length = 500, null = True, blank = True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, default=uuid.uuid4)
    invoice_id = models.CharField(max_length = 500,default=increment_invoice_number, null = True, blank = True)
    stock_dept_invoice_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Stock Dept Invoice Id")

    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    vat_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    due_date = models.DateField(default=now)

    def __str__(self):
        return self.invoice_id if self.invoice_id else 'New Purchase Order'

    def get_absolute_url(self):
        return reverse('purchase:purchase-details', args=[self.slug])

    def save(self, *args, **kwargs):
            self.slug = slugify(self.vendor)
            super(Purchase, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        self.title = str(self.vendor.company_name)+''+ str(self.created)
        order_items = self.order_items.all()
        self.amount = order_items.aggregate(Sum('total_price'))['total_price__sum'] if order_items.exists() else 0.00
        self.grand_total = self.amount - self.vat_amount
        #self.final_value = Decimal(self.value) - Decimal(self.discount)
        super().save(*args, **kwargs)


# ---- Order Signal ---- #
def purchase_signal(sender, **kwargs):
    if kwargs['created']:
        purchase_signal_trans = Purchase.objects.create(vendor=kwargs['instance'])

post_save.connect(purchase_signal, sender=Vendor)

class OrderItem(models.Model):
    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
        ('Boulangerie', 'Boulangerie'),
        ('Supermarket', 'Supermarket'),
        ('Bar', 'Bar'),
        ('Snack', 'Snack'),
        ('Ice Cream', 'Ice Cream'),

    )
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    purchase_order = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='order_items')
    product = models.CharField(max_length = 500, null = True, blank = True)
    qty = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    final_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    total_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)

    def __str__(self):
        return f'{self.total_price}'
        #return f'{self.product.name}'

    def price_total_net(self):
        return ((self.qty) * (self.price))

    def save(self,  *args, **kwargs):
        #self.price = self.product.price
        #self.final_price = self.discount_price if self.discount_price > 0 else self.price
        #self.total_price = Decimal(self.qty) * Decimal(self.final_price)
        self.total_price = self.price_total_net
        super().save(*args, **kwargs)
        self.purchase_order.save()


def increment_payment_number():
    last_payment = Payment.objects.all().order_by('id').last()
    if not last_payment:
         return 'PAY0001'
    payment_id = last_payment.payment_id
    payment_int = int(payment_id.split('PAY000')[-1])
    new_payment_int = payment_int + 1
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")
    new_payment_id = today_string + "-" + 'PAY000'  + str(new_payment_int)
    return new_payment_id

class Payment(models.Model):
    PAYMENTINSTALLMENTS = (
        ('1st Installment', '1st Installment'),
        ('2nd Installment', '2nd Installment'),
        ('3rd Installment', '3rd Installment'),
        ('4th Installment', '4th Installment'),
        ('5th Installment', '5th Installment'),
        ('6th Installment', '6th Installment'),
        ('7th Installment', '7th Installment'),
        ('8th Installment', '8th Installment'),
        ('9th Installment', '9th Installment'),
        ('10th Installment', '10th Installment'),
        ('11th Installment', '11th Installment'),
        ('12th Installment', '12th Installment'),
        ('13th Installment', '13th Installment'),
        ('14th Installment', '14th Installment'),
        ('15th Installment', '15th Installment'),
        ('16th Installment', '16th Installment'),
        ('17th Installment', '17th Installment'),
    )

    created = models.DateField(default=now)
    employee = models.CharField(max_length = 500, null = True, blank = True)
    #vendor= models.ForeignKey(Vendor, on_delete=models.CASCADE)
    invoice_id = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, blank=True, default=uuid.uuid4)
    installment = models.CharField(max_length=20, choices=PAYMENTINSTALLMENTS, default='1st Installment', null = True, blank = True)
    invoice_number = models.CharField(max_length = 500, null = True, blank = True)
    invoice_amount = models.IntegerField(default=0)
    payment_id = models.CharField(max_length = 500, default=increment_payment_number, null = True, blank = True)
    amount_paid = models.IntegerField(default=0)

    balance_due = models.IntegerField(default=0)
    status =  models.CharField(max_length = 500, null = True, blank = True)


    def __str__(self):
        return str(self.invoice_id.vendor)

    @property
    def get_balance_due(self):
        if self.created:
            return self.invoice_amount - self.amount_paid
            return

    @property
    def get_status(self):
        if self.amount_paid == self.invoice_amount:
            return 'Fully Paid'
        elif self.amount_paid < self.invoice_amount:
            return 'Patially Paid'

        else:
            return 'Fully Paid'
            return

    def save(self, *args, **kwargs):
        self.balance_due = self.get_balance_due
        self.status = self.get_status
        super(Payment, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

# ---- Payment Signal ---- #
def payment_signal(sender, **kwargs):
    if kwargs['created']:
        return_signal_trans = Payment.objects.create(invoice_id=kwargs['instance'])

post_save.connect(payment_signal, sender=Purchase)
