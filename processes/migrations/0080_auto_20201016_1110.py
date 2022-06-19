# Generated by Django 3.0.8 on 2020-10-16 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0079_auto_20201016_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process_8_2',
            name='q1',
        ),
        migrations.RemoveField(
            model_name='process_8_2',
            name='q2',
        ),
        migrations.RemoveField(
            model_name='process_8_2',
            name='q3',
        ),
        migrations.RemoveField(
            model_name='process_8_2',
            name='q4',
        ),
        migrations.AddField(
            model_name='process_8',
            name='q1111',
            field=models.IntegerField(blank=True, choices=[(0, 'OK'), (1, 'CONDITIONAL ADMISSION'), (2, 'RED')], default=0, verbose_name='Result'),
        ),
        migrations.AddField(
            model_name='process_8',
            name='q2222',
            field=models.IntegerField(blank=True, choices=[(0, 'Rexroth'), (1, 'Not Tested')], default=0, verbose_name='Rework'),
        ),
        migrations.AddField(
            model_name='process_8',
            name='q3333',
            field=models.IntegerField(blank=True, choices=[(0, 'Aydın Kongel'), (1, 'Ferdi Akdemir')], default=0, verbose_name='Controller'),
        ),
        migrations.AddField(
            model_name='process_8',
            name='q4444',
            field=models.IntegerField(blank=True, choices=[(0, 'Aydın Kongel'), (1, 'Ferdi Akdemir')], default=0, verbose_name='Approving Person'),
        ),
    ]
