# Generated by Django 4.0.4 on 2022-04-22 20:22

import bakerycustomersinvoices.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakerycustomersinvoices', '0066_alter_invoice_invoice_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_id',
            field=models.CharField(blank=True, default=bakerycustomersinvoices.models.increment_invoice_number, max_length=500, null=True),
        ),
    ]
