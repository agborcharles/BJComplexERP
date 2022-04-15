# Generated by Django 3.2.2 on 2022-04-08 18:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_accounting', '0019_remove_bakeryrmreturns_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='BakeryCustomers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Customers')),
                ('busness_type', models.CharField(blank=True, choices=[('Sole Proprietor', 'Sole Proprietor'), ('Supplier', 'Supplier'), ('Institution', 'Institution')], max_length=500, null=True, verbose_name='busness_type')),
                ('quarter', models.CharField(blank=True, max_length=500, null=True, verbose_name='quarter')),
                ('street', models.CharField(blank=True, max_length=500, null=True, verbose_name='street')),
                ('gps_long', models.CharField(blank=True, max_length=500, null=True, verbose_name='gps_long')),
                ('gps_lat', models.CharField(blank=True, max_length=500, null=True, verbose_name='gps_lat')),
                ('phone_1', models.CharField(blank=True, max_length=500, null=True, verbose_name='phone_1')),
                ('phone_2', models.CharField(blank=True, max_length=500, null=True, verbose_name='phone_2')),
                ('road_street_location', models.CharField(blank=True, max_length=500, null=True, verbose_name='Road Street Location')),
            ],
        ),
    ]
