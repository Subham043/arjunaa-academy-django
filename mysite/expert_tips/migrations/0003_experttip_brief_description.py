# Generated by Django 4.1.7 on 2023-03-05 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert_tips', '0002_alter_experttip_slug_alter_experttip_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='experttip',
            name='brief_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
