# Generated by Django 4.1 on 2023-03-10 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_alter_payment_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
    ]
