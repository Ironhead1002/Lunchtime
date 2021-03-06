# Generated by Django 4.0.3 on 2022-04-03 07:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('canteenInfo', '0002_alter_canteeninfo_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canteeninfo',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2022, 4, 3, 8, 28, 36, 263002, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='canteeninfo',
            name='last_scan_date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 3, 7, 58, 36, 262879, tzinfo=utc)),
        ),
    ]
