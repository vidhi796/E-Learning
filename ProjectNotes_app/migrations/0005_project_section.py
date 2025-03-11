# Generated by Django 5.1.1 on 2024-10-03 18:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectNotes_app', '0004_rename_notes_notes_section'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Section',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Frontend', 'Frontend'), ('Fullstack', 'Fullstack'), ('Theme', 'Theme')], max_length=50, verbose_name='Category of Projects')),
                ('slug', models.CharField(max_length=150, verbose_name='Url - Name')),
                ('Project_name', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(blank=True, verbose_name='Project Created Date')),
                ('project_image', models.ImageField(blank=True, upload_to='Project_documents/images')),
                ('headline_1', models.CharField(default=None, max_length=80, null=True)),
                ('headline_2', models.CharField(default=None, max_length=80, null=True)),
                ('headline_3', models.CharField(default=None, max_length=80, null=True)),
                ('headline_4', models.CharField(default=None, max_length=80, null=True)),
                ('Project_content', models.TextField(default=None, null=True)),
                ('Project_Code', models.CharField(default=None, max_length=80, null=True)),
                ('Publisher_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Teacher Name')),
            ],
            options={
                'verbose_name': 'All kind of Project',
                'verbose_name_plural': 'All kind of Projects',
            },
        ),
    ]
