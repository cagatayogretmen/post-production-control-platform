# Generated by Django 3.0.8 on 2020-10-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0068_auto_20201014_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_2',
            name='q1',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='I received the product file for pre assembly.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q10',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Pumps are OK'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q11',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Bellhousng is suitable for pumps and electric motors.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q12',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Couplings are OK for pumps and electric motors.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q13',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Pumps flanges are OK'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q14',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Pressure filter is OK.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q15',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Return filter is OK.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q16',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Three way valve is OK for return line'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q17',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Accumulator/Accumulators are OK.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q18',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Accumulator assembly parts are OK'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q19',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name="Accumulator's safety block is OK"),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q2',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='I received the oil tank.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q20',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Cooling size is OK for assembly'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q21',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Compensator is OK'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q22',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Butterfly valves are OK.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q23',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Tank drain valve is OK'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q24',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Heater  is OK and there is no problem for tank assembly.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q25',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Level gauge is OK'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q26',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Level gauge with switch is OK.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q27',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Manometer type and size is  OK'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q28',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Flange connections are OK'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q29',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Stainless fittings and pipes are OK.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q3',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='I received the valve stand.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q30',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Silica gel / air filter is OK'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q31',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Terminal box is OK'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q4',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='I received the accumulator stand.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q5',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='All assembly parts are correct and there is no missing part'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q6',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Tank cover is Ok'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q7',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='I received the blocks for power unit.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q8',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Electrical motor is checked size and power is OK'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q9',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Electric motor damping rods are OK'),
        ),
    ]
