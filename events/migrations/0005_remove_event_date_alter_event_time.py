# Generated by Django 4.1.2 on 2022-11-09 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_delete_speaker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 15, 28, 18, 469589)),
        ),
    ]