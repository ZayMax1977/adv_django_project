# Generated by Django 4.1.7 on 2023-04-01 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_postlist_url_address_alter_postlist_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlist',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_ok', to='posts.postlist'),
        ),
    ]
