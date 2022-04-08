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

from django.db.models import Sum
from django.conf import settings
from django.urls import reverse
from django.dispatch import receiver
# phone validator using regular expressions
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message='Phone number invalid. Should start with example: +237'
)

class Customer(models.Model):

    Customer_TYPE = (
        ('Company', 'Company'),
        ('Enterprise', 'Enterprise'),
        ('Individual', 'Individual'),
        ('School', 'School'),
        ('NGOs', 'NGOs'),
    )
    '''General information fields'''
    created = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=200)
    customer_type = models.CharField(max_length=10, choices=Customer_TYPE)
    company_name = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    '''Contact details fields'''
    address = models.TextField(max_length=255, null=True, verbose_name = "Address")
    city = models.CharField(max_length=100, default='Kumba', verbose_name = "City")
    region = models.CharField(max_length=200, default='South West Region', verbose_name = "Region")
    phone = models.CharField(validators=[phone_regex], max_length=15, null=True, verbose_name = "Phone")
    email = models.EmailField(blank=True, null=True, verbose_name = "Email")

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.customer_name


    def get_absolute_url(self):
        return reverse('bakerycustomersinvoices:customer-details', args=[self.slug])

    def save(self, *args, **kwargs):
            self.slug = slugify(self.customer_name)
            super(Customer, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']


class CustomerOpeningBalance(models.Model):
    created = models.DateField(default=now)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.customer)

    class Meta:
        ordering = ['-created']

# ---- OpeningBalance Signal ---- #
def customer_opening_balance(sender, **kwargs):
    if kwargs['created']:
        customer_opening_balance_trans = CustomerOpeningBalance.objects.create(customer=kwargs['instance'])

post_save.connect(customer_opening_balance, sender=Customer)




#---------------------- Invoice Number for Invoice Model----------------------#

def increment_invoice_number():
    last_invoice = Invoice.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice:
            return today_string + "-" + 'INV0001'

    invoice_id = last_invoice.invoice_id
    invoice_int = int(invoice_id.split('INV000')[-1])
    new_invoice_int = invoice_int + 1

    new_invoice_id = today_string + "-" + 'INV000'  + str(new_invoice_int)
    return new_invoice_id


class Invoice(models.Model):
    Sales_Session = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )
    created = models.DateField(default=now)
    sales_session =  models.CharField(max_length = 500, choices=Sales_Session,  default='Morning', null = True, blank = True, verbose_name ="Session")
    stock_manager = models.CharField(max_length = 500, null = True, blank = True, verbose_name = "Procurement Manager")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name ="Customer")
    invoice_id = models.CharField(max_length = 500,default=increment_invoice_number, null = True, blank = True)
    stock_dept_invoice_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Stock Dept Invoice Id")
    slug = models.SlugField(max_length=100, unique=True, blank=True, default=uuid.uuid4)
    # Total field for each invoice
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    net_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    due_date = models.DateField(default=now)
    def __str__(self):
        return self.invoice_id

# ---- Order Signal ---- #
# ---- OrderItems Signal ---- #
def invoice_signal(sender, **kwargs):
    if kwargs['created']:
        invoice_signal_trans = Invoice.objects.create(customer=kwargs['instance'])
post_save.connect(invoice_signal, sender=Customer)


class InvoiceItem(models.Model):
    created = models.DateField(default=now)
    invoice_id = models.CharField(max_length=100, default='')
    stock_manager = models.CharField(max_length = 500, null = True, blank = True, verbose_name = "Procurement Manager")
    category = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=100, default='')
    product = models.CharField(max_length=100, default='')
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    @property
    def price_total_net(self):
        return (Decimal(self.quantity) * Decimal(self.price)) - (Decimal(self.quantity) * Decimal(self.discount))

    # Overriding the save method to update invoice total for each new item
    def save(self, *args, **kwargs):
        self.price = self.price
        self.total = self.price_total_net
        #self.total_amount = order_items.aggregate(Sum('total_price'))['total_price__sum'] if order_items.exists() else 0.00
        #self.invoice.save()
        super().save(*args, **kwargs)

# ---- OrderItems Signal ---- #
#def invoice_items_signal(sender, **kwargs):
    #if kwargs['created']:
        #invoice_items_signal_trans = InvoiceItem.objects.create(invoice=kwargs['instance'])
#post_save.connect(invoice_items_signal, sender=Invoice)

# ----------------- Order Signal ------------- #
def increment_invoice_number():
    last_invoice_payment = InvoicePayment.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice_payment:
            return today_string + "-" + 'PAYMT0001'

    payment_id = last_invoice_payment.payment_id
    payment_int = int(payment_id.split('PAYMT000')[-1])
    new_payment_int = payment_int + 1

    new_payment_id = today_string + "-" + 'PAYMT000'  + str(new_payment_int)
    return new_payment_id

class InvoicePayment(models.Model):
    Payment_Installment = (
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

    )

    Payment_Session = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )
    created = models.DateField(default=now)
    payment_session =  models.CharField(max_length = 500, choices=Payment_Session,  default='Morning', null = True, blank = True)
    payment_installment =  models.CharField(max_length = 500, choices=Payment_Installment,  default='1st Installment', null = True, blank = True)
    payment_id = models.CharField(max_length = 500,default=increment_invoice_number, null = True, blank = True)
    employee = models.CharField(max_length = 500, null = True, blank = True)
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length = 500, null = True, blank = True)
    invoice_amount =  models.DecimalField(max_digits=20, decimal_places=2, default=0)
    amount_paid = models.DecimalField(max_digits=20, decimal_places=2, default=0)


    def __str__(self):
        return self.payment_id

    @property
    def total_amount(self):
        return self.invoice.grand_total

    def save(self, *args, **kwargs):
        #self.invoice_amount = self.invoice.grand_total
        super().save(*args, **kwargs)

# ---- OrderItems Signal ---- #
def invoice_payment_signal(sender, **kwargs):
    if kwargs['created']:
        invoice_payment_signal_trans = InvoicePayment.objects.create(invoice=kwargs['instance'])
post_save.connect(invoice_payment_signal, sender=Invoice)
