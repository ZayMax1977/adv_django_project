# Generated by Django 4.1.7 on 2023-03-06 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_adv', '0015_alter_adv_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='adv',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
