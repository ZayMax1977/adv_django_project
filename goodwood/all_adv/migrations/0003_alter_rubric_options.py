# Generated by Django 4.1.7 on 2023-03-03 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all_adv', '0002_rubric_alter_adv_options_alter_adv_content_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rubric',
            options={'verbose_name': 'Рубрика', 'verbose_name_plural': 'Рубрики'},
        ),
    ]
