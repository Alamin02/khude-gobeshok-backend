# Generated by Django 2.2.3 on 2019-09-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.URLField(blank=True),
        ),
    ]
