# Generated by Django 4.1.7 on 2023-03-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_blog_slug_alter_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='brief_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]