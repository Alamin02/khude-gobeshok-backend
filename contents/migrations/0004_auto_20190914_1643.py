# Generated by Django 2.2.3 on 2019-09-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_auto_20190822_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThumbnailImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='ThumbnailImage2',
        ),
    ]
