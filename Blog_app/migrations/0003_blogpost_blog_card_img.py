# Generated by Django 5.1.1 on 2024-10-03 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0002_alter_blogpost_created_at_alter_blogpost_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='blog_card_img',
            field=models.ImageField(blank=True, upload_to='blog/images'),
        ),
    ]
