# Generated by Django 2.2.3 on 2020-05-04 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process_3',
            name='content',
        ),
        migrations.RemoveField(
            model_name='process_3',
            name='soru1',
        ),
        migrations.RemoveField(
            model_name='process_3',
            name='soru2',
        ),
        migrations.RemoveField(
            model_name='process_3',
            name='soru3',
        ),
        migrations.RemoveField(
            model_name='process_3',
            name='soru4',
        ),
        migrations.RemoveField(
            model_name='process_3',
            name='soru5',
        ),
        migrations.AddField(
            model_name='process_3',
            name='q1',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Hidrolik Güç Ünitesi izlenebilirlik etiketi takılmıştır.'),
        ),
        migrations.AddField(
            model_name='process_3',
            name='q10',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Hidrolik Güç Ünitesi izlenebilirlik etiketi takılmıştır.'),
        ),
        migrations.AddField(
            model_name='process_3',
            name='q11',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Montajçılar, kaynakçılar ve testçiler ünite izlenebilirlik kartını işaretlemişlerdir'),
        ),
        migrations.AddField(
            model_name='process_3',
            name='q12',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Hidrolik Güç Ünitesinde (HGÜ) herhangi bir görsel uygunsuzluk (darbe, kirlilik, pas, boya) yoktur.'),
        ),
        migrations.AddField(
            model_name='process_3',
            name='q2',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Montajçılar, kaynakçılar ve testçiler ünite izlenebilirlik kartını işaretlemişlerdir'),
        ),
        migrations.AddField(
            model_name='process_3',
            name='q3',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Hidrolik Güç Ünitesinde (HGÜ) herhangi bir görsel uygunsuzluk (darbe, kirlilik, pas, boya) yoktur.'),
        ),
        migrations.AddField(
            model_name='process_3',
            name='q4',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Hidrolik Güç Ünitesi izlenebilirlik etiketi takılmıştır.'),
        ),
        migrations.AddField(
            model_name='process_3',
            name='q5',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Montajçılar, kaynakçılar ve testçiler ünite izlenebilirlik kartını işaretlemişlerdir'),
        ),
        migrations.AddField(
            model_name='process_3',
            name='q6',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Hidrolik Güç Ünitesinde (HGÜ) herhangi bir görsel uygunsuzluk (darbe, kirlilik, pas, boya) yoktur.'),
        ),
        migrations.AddField(
            model_name='process_3',
            name='q7',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Hidrolik Güç Ünitesi izlenebilirlik etiketi takılmıştır.'),
        ),
        migrations.AddField(
            model_name='process_3',
            name='q8',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Montajçılar, kaynakçılar ve testçiler ünite izlenebilirlik kartını işaretlemişlerdir'),
        ),
        migrations.AddField(
            model_name='process_3',
            name='q9',
            field=models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Not relevant')], default=0, verbose_name='Hidrolik Güç Ünitesinde (HGÜ) herhangi bir görsel uygunsuzluk (darbe, kirlilik, pas, boya) yoktur.'),
        ),
    ]
