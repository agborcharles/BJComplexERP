# Generated by Django 3.2.2 on 2022-03-21 11:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaries',
            name='transaction_id',
            field=models.CharField(blank=True, default=uuid.UUID('06aa4e49-da87-458f-bc91-a9ae06cf02a0'), max_length=500, null=True),
        ),
    ]
