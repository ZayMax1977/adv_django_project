# Generated by Django 4.1.7 on 2023-03-19 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all_adv', '0007_alter_adv_street'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adv',
            name='district_region',
        ),
    ]
