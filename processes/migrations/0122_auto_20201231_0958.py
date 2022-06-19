# Generated by Django 3.0.8 on 2020-12-31 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0121_auto_20201231_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_8',
            name='q1',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], verbose_name='Cleanliness,Oil,Paint Failure'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q10',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], verbose_name='Documentation'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q11',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], verbose_name='Lifting Eyes'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q12',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], verbose_name='Traceability Labe'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q13',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], verbose_name='Marker of Prod. Employee'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q14',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], verbose_name='Other Assembly Part Package'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q2',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], verbose_name='Deformation, Rust'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q3',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], verbose_name='Open holes closed'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q4',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], verbose_name='Missing Component'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q5',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], verbose_name='Hose Press Limit / Security Rope'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q7',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], verbose_name='WARNING Labels'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q8',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], verbose_name='Press. Filter Flow Direction'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q9',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], verbose_name='Oil Leakage'),
        ),
        migrations.AlterField(
            model_name='process_8_2',
            name='q1111',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'Conditionally Approved'), (2, 'RED')], verbose_name='Result'),
        ),
    ]