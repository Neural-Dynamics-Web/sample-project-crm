# Generated by Django 4.1 on 2023-03-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_alter_deal_assignee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='telegram',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Telegram'),
        ),
    ]
