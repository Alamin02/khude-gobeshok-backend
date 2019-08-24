# Generated by Django 2.2.3 on 2019-08-22 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_auto_20190813_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThumbnailImage2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('caption', models.CharField(blank=True, max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='ThumbnailImage',
        ),
    ]
