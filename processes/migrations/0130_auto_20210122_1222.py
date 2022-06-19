# Generated by Django 3.0.8 on 2021-01-22 09:22

from django.db import migrations, models
import processes.models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0129_auto_20210122_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process_7',
            name='picture1',
        ),
        migrations.RemoveField(
            model_name='process_7',
            name='picture2',
        ),
        migrations.RemoveField(
            model_name='process_7',
            name='picture3',
        ),
        migrations.RemoveField(
            model_name='process_7',
            name='picture4',
        ),
        migrations.AddField(
            model_name='process_7',
            name='p1',
            field=models.ImageField(blank=True, null=True, upload_to=processes.models.Process7_image, verbose_name='Upload Image 1'),
        ),
        migrations.AddField(
            model_name='process_7',
            name='p2',
            field=models.ImageField(blank=True, null=True, upload_to=processes.models.Process7_image, verbose_name='Upload Image 2'),
        ),
        migrations.AddField(
            model_name='process_7',
            name='p3',
            field=models.ImageField(blank=True, null=True, upload_to=processes.models.Process7_image, verbose_name='Upload Image 3'),
        ),
        migrations.AddField(
            model_name='process_7',
            name='p4',
            field=models.ImageField(blank=True, null=True, upload_to=processes.models.Process7_image, verbose_name='Upload Image 4'),
        ),
    ]
