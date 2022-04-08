# Generated by Django 3.2.2 on 2022-04-06 17:59

import bakerycustomersinvoices.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakerycustomersinvoices', '0030_alter_invoice_invoice_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_id',
            field=models.CharField(blank=True, default=bakerycustomersinvoices.models.increment_invoice_number, max_length=500, null=True),
        ),
    ]
