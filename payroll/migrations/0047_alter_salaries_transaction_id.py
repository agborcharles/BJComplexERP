# Generated by Django 3.2.2 on 2022-04-08 06:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0046_alter_salaries_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaries',
            name='transaction_id',
            field=models.CharField(blank=True, default=uuid.UUID('1ba08147-3233-49cb-96a6-85ffd1204db5'), max_length=500, null=True),
        ),
    ]
