# Generated by Django 4.1.2 on 2022-12-27 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_involved', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='image',
            field=models.FileField(blank=True, upload_to='publication'),
        ),
    ]
