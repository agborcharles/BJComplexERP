# Generated by Django 3.2.2 on 2022-04-07 02:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0036_alter_salaries_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaries',
            name='transaction_id',
            field=models.CharField(blank=True, default=uuid.UUID('64a11210-d74a-4e0a-bd39-20d3b0e337f3'), max_length=500, null=True),
        ),
    ]
