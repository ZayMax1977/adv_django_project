# Generated by Django 4.1.7 on 2023-03-19 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('all_adv', '0004_alter_adv_district_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adv',
            name='district_city',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Район города'),
        ),
        migrations.AlterField(
            model_name='adv',
            name='district_region',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Район субъекта'),
        ),
        migrations.AlterField(
            model_name='adv',
            name='ower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='all_adv.subject', verbose_name='Субъект'),
        ),
    ]
