# Generated by Django 2.2.3 on 2020-04-30 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200419_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='user_pictures'),
        ),
    ]
