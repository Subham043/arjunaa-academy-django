# Generated by Django 4.1.7 on 2023-03-04 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achievers', '0002_rename_results_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='banner',
            new_name='image',
        ),
    ]
