# Generated by Django 4.1.7 on 2023-03-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_adv', '0010_alter_subrubric_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subrubric',
            name='name',
            field=models.TextField(db_index=True, max_length=70, verbose_name='Подрубрика'),
        ),
    ]
