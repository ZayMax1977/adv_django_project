# Generated by Django 4.1.7 on 2023-03-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_adv', '0009_alter_adv_car_color_alter_adv_car_engine_capacity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adv',
            name='content',
            field=models.TextField(db_index=True, help_text='Не более 5000 символов', max_length=5000, null=True, verbose_name='Описание'),
        ),
    ]
