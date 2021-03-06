# Generated by Django 2.2.3 on 2020-05-04 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('processes', '0004_auto_20200504_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process_8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'In Process'), (1, 'Controlled')], default=0)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('soru1', models.IntegerField(choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0)),
                ('soru2', models.IntegerField(choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0)),
                ('soru3', models.IntegerField(choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0)),
                ('soru4', models.IntegerField(choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0)),
                ('soru5', models.IntegerField(choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0)),
                ('content', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_process8', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_process8', to='processes.Product')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
