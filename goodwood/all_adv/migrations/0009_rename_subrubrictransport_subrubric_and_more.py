# Generated by Django 4.1.7 on 2023-03-05 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all_adv', '0008_rename_subrubric_subrubrictransport_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubRubricTransport',
            new_name='SubRubric',
        ),
        migrations.RenameField(
            model_name='adv',
            old_name='sub_rubric_transport',
            new_name='sub_rubric',
        ),
    ]
