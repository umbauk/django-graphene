# Generated by Django 2.1.4 on 2020-11-08 07:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0006_auto_20201108_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 8, 7, 1, 5, 156636, tzinfo=utc)),
        ),
    ]