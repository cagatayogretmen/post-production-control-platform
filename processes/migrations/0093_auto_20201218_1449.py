# Generated by Django 3.0.8 on 2020-12-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0092_auto_20201218_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_4',
            name='q7',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='I checked root after root pass of pipe welding. If there is sagging, I cleaned it with stone engine, grinder.'),
        ),
    ]