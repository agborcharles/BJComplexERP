from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.template.defaultfilters import slugify
import uuid

# Create your models here.
# Create your models here.
class SupermarketReturnsDamages(models.Model):
    SESSION = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )

    STATUS = (
        ('Return Inwards', 'Return Inwards'),
        ('Return Outwards', 'Return Outwards'),
        ('Damages', 'Damages'),
        ('Expired', 'Expired'),
    )

    created_at = models.DateField("Date", default=now)
    department =  models.CharField(max_length = 500, default='Supermarket', null = True, blank = True, verbose_name = 'Department')
    session =  models.CharField(max_length = 500, choices=SESSION, default='', null = True, blank = True, verbose_name = 'Session')
    sales_person =  models.CharField(max_length=200, verbose_name = 'Sales Person')
    status =  models.CharField(max_length=200, choices=STATUS, default='', null = True, blank = True, verbose_name = 'Sales Person')
    category = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Category")
    product =  models.CharField(max_length=200, verbose_name = 'Product')
    qty=  models.FloatField(default=0.0, verbose_name = 'Quantity')
    unit_cost_price = models.FloatField(default=0.0, verbose_name = 'Unit Cost Price')
    total_cost_price = models.FloatField(default=0.0, verbose_name = 'Total Cost Price')

    @property
    def get_total_cost_price(self):
        return self.qty * self.unit_cost_price

    #---------------- Value Calculations -----------------#

    def save(self, *args, **kwargs):
        self.total_cost_price= self.get_total_cost_price

        super(SupermarketReturnsDamages, self).save(*args, **kwargs)

    #def get_absolute_url(self):
        #return reverse('general_ledger:transaction-details', args=[self.slug])

    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'Supermarket-Returns-Damages'
        verbose_name_plural = 'Supermarket-Returns-Damages'
        ordering: ['date']


class SupermarketSales(models.Model):
    SESSION = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )

    created_at = models.DateField("Date", default=now)
    department =  models.CharField(max_length = 500, default='Supermarket', null = True, blank = True, verbose_name = 'Department')
    session =  models.CharField(max_length = 500, choices=SESSION, default='', null = True, blank = True, verbose_name = 'Session')
    sales_person =  models.CharField(max_length=200, verbose_name = 'Sales Person')
    category = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Category")
    product =  models.CharField(max_length=200, verbose_name = 'Product')
    qty=  models.FloatField(default=0.0, verbose_name = 'Quantity')
    unit_cost_price = models.FloatField(default=0.0, verbose_name = 'Unit Cost Price')
    unit_selling_price = models.FloatField(default=0.0, verbose_name = 'Unit Selling Price')
    total_cost_price = models.FloatField(default=0.0, verbose_name = 'Total Cost Price')
    total_selling_price = models.FloatField(default=0.0, verbose_name = 'Total Selling Price')
    gross_profit = models.FloatField(default=0.0, verbose_name = 'Gross Profit')
    margin = models.FloatField(default=0.0, verbose_name = 'margin')

    @property
    def get_total_cost_price(self):
        return self.qty * self.unit_cost_price

    @property
    def get_total_selling_price(self):
        return self.qty * self.unit_selling_price

    @property
    def get_gross_profit(self):
        return self.total_selling_price - self.total_cost_price

    @property
    def get_margin(self):
        return self.gross_profit / self.unit_selling_price
    #---------------- Value Calculations -----------------#

    def save(self, *args, **kwargs):
        self.total_cost_price= self.get_total_cost_price
        self.total_selling_price= self.get_total_selling_price
        self.gross_profit= self.get_gross_profit
        self.margin= self.get_margin

        super(SupermarketSales, self).save(*args, **kwargs)

    #def get_absolute_url(self):
        #return reverse('general_ledger:transaction-details', args=[self.slug])

    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'Supermarket Sales'
        verbose_name_plural = 'Supermarket Sales'
        ordering: ['date']
