# Generated by Django 3.0.8 on 2020-12-31 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0120_auto_20201227_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process_8',
            name='q1111',
        ),
        migrations.RemoveField(
            model_name='process_8',
            name='q2222',
        ),
        migrations.RemoveField(
            model_name='process_8',
            name='q3333',
        ),
        migrations.RemoveField(
            model_name='process_8',
            name='q4444',
        ),
        migrations.AddField(
            model_name='process_8_2',
            name='q1111',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'Conditionally Approved'), (2, 'RED')], default=0, verbose_name='Result'),
        ),
        migrations.AddField(
            model_name='process_8_2',
            name='q3333',
            field=models.CharField(default=' ', max_length=200, verbose_name='Controller'),
        ),
        migrations.AddField(
            model_name='process_8_2',
            name='q4444',
            field=models.CharField(default=' ', max_length=200, verbose_name='Approving Person'),
        ),
        migrations.AlterField(
            model_name='process_1',
            name='q1111',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'Conditionally Approved'), (2, 'RED')], verbose_name='Decision'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q1',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], default=0, verbose_name='Cleanliness,Oil,Paint Failure'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q10',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], default=0, verbose_name='Documentation'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q11',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], default=0, verbose_name='Lifting Eyes'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q12',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], default=0, verbose_name='Traceability Labe'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q13',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], default=0, verbose_name='Marker of Prod. Employee'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q14',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], default=0, verbose_name='Other Assembly Part Package'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q2',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], default=0, verbose_name='Deformation, Rust'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q3',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], default=0, verbose_name='Open holes closed'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q4',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], default=0, verbose_name='Missing Component'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q5',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], default=0, verbose_name='Hose Press Limit / Security Rope'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q6',
            field=models.IntegerField(default=0, verbose_name='Paint Thickness'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q7',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], default=0, verbose_name='WARNING Labels'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q8',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], default=0, verbose_name='Press. Filter Flow Direction'),
        ),
        migrations.AlterField(
            model_name='process_8',
            name='q9',
            field=models.IntegerField(choices=[(0, 'OK'), (1, 'N.OK'), (2, 'Not Applicable')], default=0, verbose_name='Oil Leakage'),
        ),
    ]
