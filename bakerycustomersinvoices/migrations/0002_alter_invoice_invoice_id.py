# Generated by Django 3.2.2 on 2022-03-21 11:30

import bakerycustomersinvoices.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakerycustomersinvoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_id',
            field=models.CharField(blank=True, default=bakerycustomersinvoices.models.increment_invoice_number, max_length=500, null=True),
        ),
    ]
