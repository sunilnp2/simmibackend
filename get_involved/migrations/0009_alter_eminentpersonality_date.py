# Generated by Django 4.1.2 on 2022-11-28 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_involved', '0008_merge_20221128_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eminentpersonality',
            name='date',
            field=models.DateField(default=datetime.date(2022, 11, 28)),
        ),
    ]