# Generated by Django 3.2.2 on 2022-03-24 19:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0004_alter_salaries_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaries',
            name='transaction_id',
            field=models.CharField(blank=True, default=uuid.UUID('44a997f8-a254-4f8c-a90e-86b820f90540'), max_length=500, null=True),
        ),
    ]
