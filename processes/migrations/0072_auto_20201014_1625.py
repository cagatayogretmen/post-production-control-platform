# Generated by Django 3.0.8 on 2020-10-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0071_process_3_q12'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_3',
            name='q1',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Are the pipelines in accordance with the assembly list prefix and hydraulic circuit?'),
        ),
        migrations.AlterField(
            model_name='process_3',
            name='q10',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='If there is contact with other parts, the protection against abrasion been provided. '),
        ),
        migrations.AlterField(
            model_name='process_3',
            name='q11',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name="The hose security chains been correctly fitted? Security chain lock's ring pressed."),
        ),
        migrations.AlterField(
            model_name='process_3',
            name='q2',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Are the pipe diameters the same as stated in the hydraulic circuit?'),
        ),
        migrations.AlterField(
            model_name='process_3',
            name='q3',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Are all pipe connections (service connections) or customer connections accessible?'),
        ),
        migrations.AlterField(
            model_name='process_3',
            name='q4',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Are all hydraulic connections (screw connection of flanges and fittings) tight.'),
        ),
        migrations.AlterField(
            model_name='process_3',
            name='q5',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Are all the pipes cleaned and preserved?'),
        ),
        migrations.AlterField(
            model_name='process_3',
            name='q6',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Is there any evidence of unpermitted flattening? If there is no specific customer request, standard of DC; otherwise max. is 6% according to ko = [(Dmax – Dmin)/D ] x 100 '),
        ),
        migrations.AlterField(
            model_name='process_3',
            name='q7',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Were changes in direction avoided in piping? It should be preferably used round arches, angle fittings should be avoided.'),
        ),
        migrations.AlterField(
            model_name='process_3',
            name='q8',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='They lay down specific requirements for suction and pressure lines and were these observed? (high dynamic range)'),
        ),
        migrations.AlterField(
            model_name='process_3',
            name='q9',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='The hoses fitted professionaly. (e.g. Bend radius not too small. In case of contact with other parts scoring protector used)'),
        ),
    ]
