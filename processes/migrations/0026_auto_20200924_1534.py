# Generated by Django 3.0.8 on 2020-09-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0025_auto_20200924_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_6',
            name='q15',
            field=models.IntegerField(blank=True, choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], default=0, verbose_name='Hose connection fittings types controlled'),
        ),
    ]