# Generated by Django 4.1.7 on 2023-03-05 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0003_alter_enquiry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 3, 5, 17, 31, 32, 978527)),
        ),
    ]
