# Generated by Django 4.1 on 2023-04-06 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0012_deal_actual_end_date_deal_development_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date'),
        ),
    ]
