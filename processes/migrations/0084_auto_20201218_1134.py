# Generated by Django 3.0.8 on 2020-12-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0083_remove_process_2_2_q19'),
    ]

    operations = [
        migrations.AddField(
            model_name='process_1',
            name='q2',
            field=models.CharField(default='', max_length=200, verbose_name='Stainless Steel/Aluminium Quality'),
        ),
        migrations.AlterField(
            model_name='process_1',
            name='q1',
            field=models.CharField(max_length=200, verbose_name='Supplier'),
        ),
        migrations.AlterField(
            model_name='product',
            name='customer_order_no',
            field=models.IntegerField(verbose_name='Customer Order No: '),
        ),
        migrations.AlterField(
            model_name='product',
            name='imageno',
            field=models.CharField(blank=True, default=0, max_length=200, verbose_name='Oil Tank Drawing No:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='order_position_no',
            field=models.IntegerField(verbose_name='Order Position No: '),
        ),
        migrations.AlterField(
            model_name='product',
            name='tank_reference_no',
            field=models.CharField(blank=True, default=0, max_length=200, verbose_name='Oil Tank Ref. No:'),
        ),
    ]