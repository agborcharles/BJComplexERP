# Generated by Django 3.2.2 on 2022-04-08 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_list', '0002_auto_20220408_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='bank_account_no_1',
            field=models.CharField(default='', max_length=100, verbose_name='Bank Account No 1'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='bank_account_no_2',
            field=models.CharField(default='', max_length=100, verbose_name='Bank Account No 2'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='bank_name_1',
            field=models.CharField(default='', max_length=100, verbose_name='Bank Name 1'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='bank_name_2',
            field=models.CharField(default='', max_length=100, verbose_name='Bank Name 2'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='location_1',
            field=models.CharField(default='', max_length=100, verbose_name='Location 1'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='location_2',
            field=models.CharField(default='', max_length=100, verbose_name='Location 2'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile_money_account_1',
            field=models.CharField(default='', max_length=100, verbose_name='Mobile Money Account 1'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile_money_account_2',
            field=models.CharField(default='', max_length=100, verbose_name='Mobile Money Account 2'),
        ),
    ]
