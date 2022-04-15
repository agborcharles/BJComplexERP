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

class Procurement(models.Model):
    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
        ('Boulangerie', 'Boulangerie'),
        ('Supermarket', 'Supermarket'),
        ('Bar', 'Bar'),
        ('Snack', 'Snack'),
        ('Ice Cream', 'Ice Cream'),

    )
    created_at = models.DateField(default=now)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='', null = True, blank = True, verbose_name = 'Department')
    procurement_manager = models.CharField(max_length = 500, null = True, blank = True, verbose_name = "Procurement Manager")
    vendor = models.CharField(max_length = 500, null = True, blank = True)
    description = models.CharField(max_length = 500, null = True, blank = True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, default=uuid.uuid4)
    invoice_id = models.CharField(max_length = 500, null = True, blank = True)
    stock_dept_invoice_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Stock Dept Invoice Id")

    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    due_date = models.DateField(default=now)

    def __str__(self):
        return self.department

    #def get_absolute_url(self):
        #return reverse('purchase:purchase-details', args=[self.slug])

    def save(self, *args, **kwargs):
            self.slug = slugify(self.vendor)
            super(Procurement, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Procurement'
        verbose_name_plural = 'Procurement'
