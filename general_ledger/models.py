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
class GeneralLedger(models.Model):
    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
        ('Supermarket', 'Supermarket'),
        ('Bar', 'Bar'),
        ('Snack', 'Snack'),
        ('Boulangerie', 'Boulangerie'),
        ('Ice Cream', 'Ice Cream'),
    )

    EMPLOYEEMANAGEMENT = (
        ('Employee', 'Employee'),
        ('Management', 'Management'),
    )

    created_at = models.DateField("Date", default=now)
    slug = models.SlugField(max_length=100, unique=True, default=uuid.uuid4, blank=True, null=True)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='', null = True, blank = True, verbose_name = 'Department')
    employee_management =  models.CharField(max_length = 500, choices=EMPLOYEEMANAGEMENT, default='', null = True, blank = True, verbose_name = 'Employee / Management')
    transaction_id =  models.CharField(max_length=200, verbose_name = 'Transaction Id')
    reference_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Reference Id")
    institution =  models.CharField(max_length=200, verbose_name = 'Institution')
    description=  models.TextField(max_length = 2500, null = True, blank = True, verbose_name = 'Description')
    amount = models.FloatField(default=0.0, verbose_name = 'Amount')
    accounts_dr = models.CharField(max_length=200, verbose_name = 'Account Debit')
    accounts_cr = models.CharField(max_length=200, verbose_name = 'AccountsCredit')

    def get_absolute_url(self):
        return reverse('general_ledger:transaction-details', args=[self.slug])

    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'General Ledger'
        verbose_name_plural = 'General Ledger'
        ordering: ['date']
