# Generated by Django 3.0.8 on 2020-12-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0098_auto_20201223_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process_7_2',
            name='q1',
        ),
        migrations.RemoveField(
            model_name='process_7_2',
            name='q2',
        ),
        migrations.AddField(
            model_name='process_7',
            name='q1',
            field=models.CharField(blank=True, choices=[(0, 'Aydın Kongel'), (1, 'Ferdi Akdemir')], default=0, max_length=200, verbose_name='Tested By'),
        ),
        migrations.AddField(
            model_name='process_7',
            name='q2',
            field=models.CharField(blank=True, choices=[(0, 'Aydın Kongel'), (1, 'Ferdi Akdemir')], default=0, max_length=200, verbose_name='Controlled By'),
        ),
    ]