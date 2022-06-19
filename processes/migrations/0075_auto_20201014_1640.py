# Generated by Django 3.0.8 on 2020-10-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0074_auto_20201014_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_4',
            name='q1',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name="I have already taken information about the material were used for piping and oil tank' mataerial. The used WPS is selected the materials of oil tank and pipes material accordingly."),
        ),
        migrations.AlterField(
            model_name='process_4',
            name='q10',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='I cleaned surfaces and applied passivation liquied for stainless materials welding process.'),
        ),
        migrations.AlterField(
            model_name='process_4',
            name='q2',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='Before spot welding of cleaning covers of oil tank, I made spot welding and check the parameters of Welding.'),
        ),
        migrations.AlterField(
            model_name='process_4',
            name='q3',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='All surfaces were cleaned by rust, paint or oil before welding.'),
        ),
        migrations.AlterField(
            model_name='process_4',
            name='q4',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='I welded the cleaning  covers than checked the position of cleaning cover on tank.'),
        ),
        migrations.AlterField(
            model_name='process_4',
            name='q5',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='I welded the grounding element to oil tank.'),
        ),
        migrations.AlterField(
            model_name='process_4',
            name='q6',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='I applied TIG welding process for root pass of pipe. I applied the MAG welding for cover passess for pipe.'),
        ),
        migrations.AlterField(
            model_name='process_4',
            name='q7',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='I checked root after root pass of pipe welding. If there is sagging, I cleaned it with stone engine.'),
        ),
        migrations.AlterField(
            model_name='process_4',
            name='q8',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='I checked undercuts after cover pass.'),
        ),
        migrations.AlterField(
            model_name='process_4',
            name='q9',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='I checked start and finish point of MAG welds.'),
        ),
    ]