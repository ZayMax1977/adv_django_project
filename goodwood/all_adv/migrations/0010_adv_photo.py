# Generated by Django 4.1.7 on 2023-03-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_adv', '0009_adv_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='adv',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/%d/'),
        ),
    ]
