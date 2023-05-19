# Generated by Django 4.1 on 2023-02-26 07:09

from django.db import migrations, models
import utils.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('development', '0008_alter_task_risk'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PreprocessingHandlers',
        ),
        migrations.AlterField(
            model_name='feature',
            name='completion',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[utils.models.validators.positive_validator], verbose_name='Completion (%)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='completion',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[utils.models.validators.positive_validator], verbose_name='Completion (%)'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='completion',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[utils.models.validators.positive_validator], verbose_name='Completion (%)'),
        ),
    ]