# Generated by Django 4.1.7 on 2023-03-06 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_adv', '0014_adv_car_color_adv_car_mark_adv_car_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adv',
            name='title',
            field=models.CharField(help_text='Это хелп', max_length=50, verbose_name='Товар'),
        ),
    ]
