# Generated by Django 4.1.7 on 2023-03-05 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2023, 3, 5, 15, 42, 5, 844951)),
        ),
    ]