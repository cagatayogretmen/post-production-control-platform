# Generated by Django 3.0.8 on 2020-10-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0080_auto_20201016_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='process_1',
            name='q0',
            field=models.IntegerField(blank=True, default=0, verbose_name='Order Position No: '),
        ),
    ]
