# Generated by Django 3.0.8 on 2020-09-23 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0015_auto_20200923_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ident_no',
        ),
    ]
