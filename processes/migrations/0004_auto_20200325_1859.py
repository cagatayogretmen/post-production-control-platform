# Generated by Django 2.2.3 on 2020-03-25 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0003_auto_20200325_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
