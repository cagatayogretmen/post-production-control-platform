# Generated by Django 2.2.3 on 2020-05-04 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, verbose_name='Ürün ismi')),
                ('status', models.IntegerField(choices=[(0, 'In Process'), (1, 'Controlled')], default=0, verbose_name='Durum')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('production_order_no', models.CharField(blank=True, max_length=200)),
                ('order_position_no', models.CharField(blank=True, max_length=200)),
                ('reference_no', models.CharField(blank=True, max_length=200)),
                ('quantity', models.CharField(blank=True, max_length=200)),
                ('working_pressure', models.CharField(blank=True, max_length=200)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(blank=True, upload_to='product_pictures/')),
                ('content', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_product', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Process_7',
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
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_process7', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_process7', to='processes.Product')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Process_6',
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
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_process6', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_process6', to='processes.Product')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Process_5',
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
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_process5', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_process5', to='processes.Product')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Process_4',
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
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_process4', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_process4', to='processes.Product')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Process_3',
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
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_process3', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_process3', to='processes.Product')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Process_2',
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
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_process2', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_process2', to='processes.Product')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Process_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'In Process'), (1, 'Controlled')], default=0, verbose_name='Durum')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('soru1', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Hidrolik Güç Ünitesi izlenebilirlik etiketi takılmıştır.')),
                ('soru2', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Montajçılar, kaynakçılar ve testçiler ünite izlenebilirlik kartını işaretlemişlerdir')),
                ('soru3', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Hidrolik Güç Ünitesinde (HGÜ) herhangi bir görsel uygunsuzluk (darbe, kirlilik, pas, boya) yoktur.')),
                ('content', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_process1', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_process1', to='processes.Product', verbose_name='Hangi Ürün?')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]