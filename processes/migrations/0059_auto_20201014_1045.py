# Generated by Django 3.0.8 on 2020-10-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0058_auto_20201014_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stand_drawing_no',
            field=models.IntegerField(blank=True, default=0, verbose_name='Accu Stand Drawing No:'),
        ),
        migrations.AddField(
            model_name='product',
            name='stand_ref_no',
            field=models.IntegerField(blank=True, default=0, verbose_name='Accu Stand Ref. No:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, verbose_name='Quantity:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tank_reference_no',
            field=models.CharField(default=0, max_length=200, verbose_name='Oil Tank Ref. No:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.IntegerField(blank=True, default=0, verbose_name='Oil Tank Volume(lt):'),
        ),
    ]
