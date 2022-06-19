# Generated by Django 3.0.8 on 2020-10-14 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0057_auto_20201001_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='press',
        ),
        migrations.RemoveField(
            model_name='product',
            name='production_order_no',
        ),
        migrations.RemoveField(
            model_name='product',
            name='working_pressure',
        ),
        migrations.AlterField(
            model_name='product',
            name='circuitno',
            field=models.IntegerField(blank=True, default=0, verbose_name='Hydraulic Circuit No:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='customer_order_no',
            field=models.IntegerField(blank=True, default=0, verbose_name='Customer Order No: '),
        ),
        migrations.AlterField(
            model_name='product',
            name='imageno',
            field=models.CharField(default='2020/', max_length=200, verbose_name='Oil Tank Drawing No:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='order_position_no',
            field=models.IntegerField(blank=True, default=0, verbose_name='Order Position No: '),
        ),
        migrations.AlterField(
            model_name='product',
            name='reference_no',
            field=models.CharField(default='R', max_length=200, verbose_name='Reference No:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tank_reference_no',
            field=models.CharField(max_length=200, verbose_name='Oil Tank Ref. No:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.IntegerField(blank=True, default=0, verbose_name='Oil Tank Volume(lt)'),
        ),
    ]
