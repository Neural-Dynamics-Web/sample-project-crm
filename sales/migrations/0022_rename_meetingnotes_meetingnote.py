# Generated by Django 4.0 on 2023-05-02 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('development', '0029_alter_project_jira_code'),
        ('sales', '0021_alter_meetingnotes_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MeetingNotes',
            new_name='MeetingNote',
        ),
    ]
