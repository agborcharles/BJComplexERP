# Generated by Django 3.2.2 on 2022-03-21 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_accounting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bakerysales',
            name='employee',
        ),
    ]
