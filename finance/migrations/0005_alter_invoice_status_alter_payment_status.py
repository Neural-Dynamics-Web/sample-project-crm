# Generated by Django 4.1 on 2023-02-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_alter_invoice_current_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('awaiting', 'Awaiting'), ('completed', 'Completed'), ('outdated', 'Outdated')], default='waiting', max_length=255, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('awaiting', 'Awaiting'), ('completed', 'Completed'), ('outdated', 'Outdated')], default='waiting', max_length=255, verbose_name='Status'),
        ),
    ]
