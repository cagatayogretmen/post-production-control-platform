# Generated by Django 3.0.8 on 2020-09-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0024_remove_process_7_q5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_5',
            name='q6',
            field=models.IntegerField(blank=True, default=234, verbose_name='I measured the thickness of paint.'),
        ),
    ]