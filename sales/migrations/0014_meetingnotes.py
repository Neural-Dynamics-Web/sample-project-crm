# Generated by Django 4.1 on 2023-04-19 18:28

from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0013_alter_deal_end_date_alter_deal_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingNotes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', django_ckeditor_5.fields.CKEditor5Field(null=True, verbose_name='Text')),
                ('audio', models.FileField(null=True, upload_to='audio', verbose_name='Audio')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('meeting_date', models.DateField(null=True, verbose_name='Meeting Date')),
                ('deal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meeting_notes', to='sales.deal', verbose_name='Deal')),
            ],
            options={
                'verbose_name': 'Meeting Note',
                'verbose_name_plural': 'Meeting Notes',
            },
        ),
    ]