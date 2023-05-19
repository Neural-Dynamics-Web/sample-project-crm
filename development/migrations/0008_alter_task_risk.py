# Generated by Django 4.1 on 2023-02-25 16:48

from decimal import Decimal
from django.db import migrations, models
import utils.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('development', '0007_alter_task_risk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='risk',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=3, validators=[utils.models.validators.positive_validator], verbose_name='Risk'),
        ),
    ]