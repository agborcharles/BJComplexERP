# Generated by Django 3.2.2 on 2022-04-15 04:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0063_alter_salaries_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaries',
            name='transaction_id',
            field=models.CharField(blank=True, default=uuid.UUID('6a7fc566-2ead-4054-8fa3-168a579c4db7'), max_length=500, null=True),
        ),
    ]
