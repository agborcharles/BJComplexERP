# Generated by Django 4.0.4 on 2022-05-06 06:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0079_alter_salaries_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaries',
            name='transaction_id',
            field=models.CharField(blank=True, default=uuid.UUID('6c6eb2f6-f6dd-413a-9105-2b6963bf802a'), max_length=500, null=True),
        ),
    ]