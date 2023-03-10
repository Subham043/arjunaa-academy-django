# Generated by Django 4.1.7 on 2023-03-05 10:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_alter_course_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=350)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveBigIntegerField()),
                ('location', models.TextField()),
                ('request', models.CharField(choices=[('CALL_BACK', 'Call Back'), ('HOME_VISIT', 'Home Visit'), ('VISIT_OUR_CENTER', 'Visit Our Center'), ('CONNECT_ONLINE', 'Connect Online')], default='CALL_BACK', max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.TimeField(default=datetime.datetime(2023, 3, 5, 16, 4, 53, 359723))),
                ('branch', models.CharField(blank=True, choices=[('VIJAYNAGAR', 'Vijaynagar'), ('HEBBAL', 'Hebbal'), ('KANAKAPURA_ROAD', 'Kanakapura Road')], default='VIJAYNAGAR', max_length=50, null=True)),
                ('detail', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enquiries_courses', to='courses.course')),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enquiries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
