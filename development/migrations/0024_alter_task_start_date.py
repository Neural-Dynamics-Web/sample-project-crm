# Generated by Django 4.1 on 2023-03-14 06:59

from django.db import migrations, models
import utils.functions.dates


class Migration(migrations.Migration):

    dependencies = [
        ('development', '0023_alter_feature_start_date_alter_stage_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(default=utils.functions.dates.working_day, null=True, verbose_name='Start Date'),
        ),
    ]
