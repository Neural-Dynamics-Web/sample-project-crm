# Generated by Django 4.1 on 2023-03-01 10:07

from django.db import migrations, models
import utils.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('development', '0009_delete_preprocessinghandlers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='completion',
        ),
        migrations.RemoveField(
            model_name='project',
            name='completion',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='completion',
        ),
        migrations.AddField(
            model_name='feature',
            name='completion_delivery',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[utils.models.validators.positive_validator], verbose_name='Completion Delivery (%)'),
        ),
        migrations.AddField(
            model_name='feature',
            name='completion_development',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[utils.models.validators.positive_validator], verbose_name='Completion Development (%)'),
        ),
        migrations.AddField(
            model_name='project',
            name='completion_delivery',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[utils.models.validators.positive_validator], verbose_name='Completion Delivery (%)'),
        ),
        migrations.AddField(
            model_name='project',
            name='completion_development',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[utils.models.validators.positive_validator], verbose_name='Completion Development (%)'),
        ),
        migrations.AddField(
            model_name='stage',
            name='completion_delivery',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[utils.models.validators.positive_validator], verbose_name='Completion Delivery (%)'),
        ),
        migrations.AddField(
            model_name='stage',
            name='completion_development',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[utils.models.validators.positive_validator], verbose_name='Completion Development (%)'),
        ),
    ]