# Generated by Django 3.2.2 on 2022-04-07 08:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0037_alter_salaries_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaries',
            name='transaction_id',
            field=models.CharField(blank=True, default=uuid.UUID('8cff43f4-80b8-42f3-863e-50454918b6ca'), max_length=500, null=True),
        ),
    ]
