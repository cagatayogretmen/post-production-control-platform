# Generated by Django 3.0.8 on 2020-12-31 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0124_auto_20201231_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=200, verbose_name='Product Name'),
        ),
    ]