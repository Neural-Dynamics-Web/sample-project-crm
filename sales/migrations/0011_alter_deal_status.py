# Generated by Django 4.1 on 2023-04-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0010_alter_contact_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='status',
            field=models.CharField(choices=[('opened', 'Opened'), ('first_contact', 'First Contact'), ('discovery', 'Discovery'), ('evaluation', 'Evaluation'), ('document_signing', 'Document Signing'), ('win', 'Win'), ('lose', 'Lose')], default='created', max_length=255, verbose_name='Sale Status'),
        ),
    ]
