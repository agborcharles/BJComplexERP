from __future__ import unicode_literals
from django.db import models

from decimal import Decimal
from django.urls import reverse
from django.core.validators import RegexValidator, MinValueValidator

import uuid

import datetime
from django.utils.timezone import now
from django.template.defaultfilters import slugify

# phone validator using regular expressions
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message='Phone number invalid. Should start with example: +237'
)

class Contact(models.Model):

    Customer_TYPE = (
        ('Company', 'Company'),
        ('Enterprise', 'Enterprise'),
        ('Individual', 'Individual'),
        ('School', 'School'),
        ('NGOs', 'NGOs'),
    )

    CATEGORY = (
        ('Customer', 'Customer'),
        ('Supplier', 'Supplier'),
        ('Bank', 'Bank'),
        ('Technician', 'Technician'),

    )
    '''General information fields'''
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, verbose_name = "Contact Name")
    company_name = models.CharField(max_length=200, default='', blank=True, null=True, verbose_name = "Company Name")
    contact_type = models.CharField(max_length=200, choices=Customer_TYPE, default='', blank=True, null=True, verbose_name = "Company Type")
    category = models.CharField(max_length=10, choices=CATEGORY, blank=True, null=True, verbose_name = "Category")
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    '''Contact details fields'''
    street = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name = "street")
    quarter = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name = "Quarter")
    address = models.TextField(max_length=255, null=True, verbose_name = "Address")
    city = models.CharField(max_length=100, default='Kumba', verbose_name = "City")
    region = models.CharField(max_length=200, default='South West Region', verbose_name = "Region")
    phone = models.CharField(validators=[phone_regex], max_length=15, null=True, verbose_name = "Phone")
    email = models.EmailField(blank=True, null=True, verbose_name = "Email")

    tax_payer_no = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name = "Tax Payers No")

    bank_account_no_1 = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name = "Bank Account No 1")
    bank_name_1 = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name = "Bank Name 1")
    bank_accnt_name_1 = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name = "Bank Account Name 1")

    bank_account_no_2 = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name = "Bank Account No 2")
    bank_name_2 = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name = "Bank Name 2")
    bank_accnt_name_2 = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name = "Bank Account Name 2")

    mobile_money_account_1 = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name = "Mobile Money Account 1")
    mobile_money_account_2 = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name = "Mobile Money Account 2")

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('contact_list:contact-detail', args=[self.slug])

    def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Contact, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
