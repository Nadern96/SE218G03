# Generated by Django 2.1.2 on 2018-11-25 09:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0005_auto_20181125_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Address',
            field=models.CharField(default='7 Address Hotel', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='time',
            field=models.TimeField(default=datetime.datetime(2018, 11, 25, 9, 32, 53, 685159, tzinfo=utc)),
        ),
    ]
