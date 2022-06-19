# Generated by Django 3.0.8 on 2020-09-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0029_auto_20200924_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_7',
            name='q12',
            field=models.IntegerField(blank=True, choices=[(0, 'None'), (1, 'Dedected')], default=0, verbose_name='Oil Leakage'),
        ),
        migrations.AlterField(
            model_name='process_7',
            name='q13',
            field=models.IntegerField(blank=True, choices=[(0, 'Yes'), (1, 'No')], default=0, verbose_name='Missing Parts'),
        ),
    ]
