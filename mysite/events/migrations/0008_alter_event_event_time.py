# Generated by Django 4.1.7 on 2023-03-05 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_event_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2023, 3, 5, 17, 31, 32, 976421)),
        ),
    ]
