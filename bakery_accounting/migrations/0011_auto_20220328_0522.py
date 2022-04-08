# Generated by Django 3.2.2 on 2022-03-28 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_accounting', '0010_bakeryinventory_weight_per_pack'),
    ]

    operations = [
        migrations.AddField(
            model_name='bakeryinventory',
            name='direct_indirect',
            field=models.CharField(blank=True, choices=[('Direct', 'Direct'), ('Indirect', 'Indirect')], default='', max_length=500, null=True, verbose_name='Drect / Indirect'),
        ),
        migrations.AlterField(
            model_name='bakeryinventory',
            name='entry_measure',
            field=models.CharField(blank=True, choices=[('Grams', 'Grams'), ('Kg', 'Kg'), ('Unit', 'Unit'), ('Litre', 'Litre')], default='', max_length=500, null=True, verbose_name='Entry Measure'),
        ),
        migrations.AlterField(
            model_name='bakeryinventory',
            name='weight_per_pack',
            field=models.FloatField(default=0.0, verbose_name='Weight / Pack'),
        ),
    ]
