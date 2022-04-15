# Generated by Django 3.2.2 on 2022-04-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_accounting', '0021_rename_name_bakerycustomers_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bakerycustomers',
            options={'verbose_name': 'Bakery Customers', 'verbose_name_plural': 'Bakery Customers'},
        ),
        migrations.AddField(
            model_name='bakerypayment',
            name='quarter',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Quarter'),
        ),
        migrations.AddField(
            model_name='bakerypayment',
            name='street',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Street'),
        ),
    ]
