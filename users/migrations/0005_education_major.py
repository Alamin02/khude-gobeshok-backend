# Generated by Django 2.2.3 on 2019-09-06 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190906_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='major',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
