# Generated by Django 2.2.3 on 2019-09-17 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='software_skills',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='specialized_in',
            field=models.TextField(blank=True),
        ),
    ]