# Generated by Django 2.1.2 on 2018-12-08 20:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0013_auto_20181208_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='time',
            field=models.TimeField(default=datetime.datetime(2018, 12, 8, 20, 37, 41, 823300, tzinfo=utc)),
        ),
    ]
