# Generated by Django 3.0.8 on 2020-09-24 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0027_auto_20200924_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process_8',
            name='q15',
        ),
        migrations.AlterField(
            model_name='process_8_2',
            name='q2',
            field=models.IntegerField(blank=True, choices=[(0, 'Rexroth'), (1, 'Not Tested')], default=0, verbose_name='Ek İşlem'),
        ),
    ]