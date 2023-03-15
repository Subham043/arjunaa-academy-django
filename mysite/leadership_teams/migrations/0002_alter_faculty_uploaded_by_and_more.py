# Generated by Django 4.1.7 on 2023-03-15 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leadership_teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='faculties_uploaded', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='management',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managements_uploaded', to=settings.AUTH_USER_MODEL),
        ),
    ]