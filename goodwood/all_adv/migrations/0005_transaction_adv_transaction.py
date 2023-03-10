# Generated by Django 4.1.7 on 2023-03-05 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('all_adv', '0004_alter_rubric_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=21, verbose_name='Вид сделки')),
            ],
            options={
                'verbose_name': 'Вид сделки',
                'verbose_name_plural': 'Вид сделки',
            },
        ),
        migrations.AddField(
            model_name='adv',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='all_adv.transaction', verbose_name='Товар'),
        ),
    ]
