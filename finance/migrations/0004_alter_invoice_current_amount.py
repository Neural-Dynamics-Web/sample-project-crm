# Generated by Django 4.1 on 2023-02-28 09:23

from django.db import migrations, models
import utils.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_invoice_completion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='current_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[utils.models.validators.positive_validator], verbose_name='Current Amount ($)'),
        ),
    ]
