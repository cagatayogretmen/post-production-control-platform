# Generated by Django 3.0.8 on 2020-12-23 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0099_auto_20201223_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process_7',
            name='q1',
        ),
        migrations.RemoveField(
            model_name='process_7',
            name='q2',
        ),
        migrations.AddField(
            model_name='process_7_2',
            name='q1',
            field=models.CharField(blank=True, default=0, max_length=200, verbose_name='Tested By'),
        ),
        migrations.AddField(
            model_name='process_7_2',
            name='q2',
            field=models.CharField(blank=True, default=0, max_length=200, verbose_name='Controlled By'),
        ),
    ]
