# Generated by Django 4.1.2 on 2022-12-27 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_involved', '0005_remove_electronicmedia_file_electronicmedia_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electronicmedia',
            old_name='picture',
            new_name='file',
        ),
    ]
