# Generated by Django 3.2.2 on 2022-03-28 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_accounting', '0012_remove_bakerypurchase_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bakerypurchase',
            name='location',
        ),
    ]
