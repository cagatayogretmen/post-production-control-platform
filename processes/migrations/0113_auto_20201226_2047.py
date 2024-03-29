# Generated by Django 3.0.8 on 2020-12-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0112_auto_20201226_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_7',
            name='q1',
            field=models.IntegerField(choices=[(0, 'DONE'), (1, 'Not Done')], verbose_name='I check out the Hydraulic circut.'),
        ),
        migrations.AlterField(
            model_name='process_7',
            name='q2',
            field=models.IntegerField(choices=[(0, 'DONE'), (1, 'Not Done')], verbose_name='I check out the test pressure.'),
        ),
        migrations.AlterField(
            model_name='process_7',
            name='q3',
            field=models.IntegerField(choices=[(0, 'DONE'), (1, 'Not Done')], verbose_name='I check out the set up values of valves accodance with Hydraulic circut.'),
        ),
        migrations.AlterField(
            model_name='process_7',
            name='q4',
            field=models.IntegerField(choices=[(0, 'DONE'), (1, 'Not Done')], verbose_name='I checked out the ıf there special test requirements or test plans.'),
        ),
        migrations.AlterField(
            model_name='process_7',
            name='q5',
            field=models.IntegerField(choices=[(0, 'DONE'), (1, 'Not Done')], verbose_name='All electrical connections are done by electric technician.'),
        ),
        migrations.AlterField(
            model_name='process_7',
            name='q6',
            field=models.IntegerField(choices=[(0, 'DONE'), (1, 'Not Done')], verbose_name='Oil tank is filled with oil.'),
        ),
        migrations.AlterField(
            model_name='process_7',
            name='q7',
            field=models.IntegerField(choices=[(0, 'DONE'), (1, 'Not Done')], verbose_name='Im going to increase the pressure quit slowly when I start the pressure test.'),
        ),
    ]
