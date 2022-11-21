# Generated by Django 4.1.2 on 2022-11-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_alter_event_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='image_1',
            field=models.ImageField(blank=True, upload_to='events'),
        ),
    ]
