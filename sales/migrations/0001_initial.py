# Generated by Django 4.1 on 2023-02-24 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields
import phonenumber_field.modelfields
import utils.models.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('development', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_status', models.CharField(choices=[('new', 'New'), ('unqualified', 'Unqualified'), ('qualified', 'Qualified'), ('lost', 'Lost'), ('closed_deal', 'Closed Lead'), ('open_deal', 'Open Deal')], default='new', max_length=255, verbose_name='Lead Status')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True, verbose_name='Phone Number')),
                ('position', models.CharField(max_length=255, null=True, verbose_name='Position')),
                ('telegram', models.URLField(blank=True, max_length=255, null=True, unique=True, verbose_name='Telegram')),
                ('company', models.CharField(max_length=255, null=True, verbose_name='Company')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('last_call', models.DateField(blank=True, null=True, verbose_name='Last Call')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contacts', to='geo.country', verbose_name='Country')),
                ('projects', models.ManyToManyField(blank=True, related_name='contacts', to='development.project', verbose_name='Projects')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, null=True, validators=[utils.models.validators.positive_validator], verbose_name='Amount ($)')),
                ('premium', models.DecimalField(decimal_places=2, max_digits=10, null=True, validators=[utils.models.validators.positive_validator], verbose_name='Premium ($)')),
                ('staff', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salary', to=settings.AUTH_USER_MODEL, verbose_name='Staff')),
            ],
            options={
                'verbose_name': 'Salary',
                'verbose_name_plural': 'Salaries',
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Description')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, null=True, validators=[utils.models.validators.positive_validator], verbose_name='Amount ($)')),
                ('estimate', models.FileField(blank=True, null=True, upload_to='estimates', verbose_name='Estimate')),
                ('status', models.CharField(choices=[('irrelevant', 'Irrelevant'), ('awating', 'Awaiting'), ('done', 'Done')], default='created', max_length=255, verbose_name='Status')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deals', to=settings.AUTH_USER_MODEL, verbose_name='Staff')),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deals', to='sales.contact', verbose_name='Contact')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deals', to='development.project', verbose_name='Project')),
                ('stage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deals', to='development.stage', verbose_name='Stage')),
            ],
            options={
                'verbose_name': 'Deals',
                'verbose_name_plural': 'Deals',
            },
        ),
    ]