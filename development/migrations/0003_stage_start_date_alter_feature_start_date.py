# Generated by Django 4.1 on 2023-02-25 12:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('development', '0002_preprocessinghandlers_stage_max_delivery_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Date'),
        ),
    ]
