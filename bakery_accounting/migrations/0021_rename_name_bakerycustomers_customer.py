# Generated by Django 3.2.2 on 2022-04-08 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_accounting', '0020_bakerycustomers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bakerycustomers',
            old_name='name',
            new_name='customer',
        ),
    ]
