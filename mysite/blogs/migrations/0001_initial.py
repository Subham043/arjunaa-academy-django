# Generated by Django 4.1.7 on 2023-03-04 10:48

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('detail', ckeditor.fields.RichTextField()),
                ('article_for', models.CharField(choices=[('FOR_KIDS', 'Kids'), ('FOR_ADULTS', 'Adults')], default='FOR_ADULTS', max_length=50)),
                ('banner', models.ImageField(upload_to='blogs/%Y/%m/%d/')),
                ('publish_on', models.DateField(blank=True, default=datetime.date.today)),
                ('is_draft', models.BooleanField(default=False)),
                ('meta_title', models.TextField(blank=True, null=True)),
                ('og_title', models.TextField(blank=True, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('og_description', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
