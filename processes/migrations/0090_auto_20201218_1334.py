# Generated by Django 3.0.8 on 2020-12-18 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0089_auto_20201218_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='process_2_2',
            name='q19',
            field=models.TextField(blank=True, verbose_name='Remarks'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q16',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='16.Three way valve is OK and fit to Hydraulic circut.'),
        ),
        migrations.AlterField(
            model_name='process_2',
            name='q20',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No'), (2, 'Not Relavant')], verbose_name='20.Cooling type and size are OK for assembly.'),
        ),
    ]