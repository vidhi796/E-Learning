# Generated by Django 5.1.1 on 2024-10-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='updated_at',
            field=models.DateTimeField(blank=True),
        ),
    ]
