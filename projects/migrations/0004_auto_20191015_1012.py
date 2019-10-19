# Generated by Django 2.2.3 on 2019-10-15 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_profileimage'),
        ('projects', '0003_auto_20190924_0638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='project',
            name='cover_image',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contents.ThumbnailImage'),
            preserve_default=False,
        ),
    ]