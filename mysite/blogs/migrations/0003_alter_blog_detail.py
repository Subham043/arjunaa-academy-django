# Generated by Django 4.1.7 on 2023-03-04 10:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog_delete_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]