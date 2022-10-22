# Generated by Django 4.1.2 on 2022-10-22 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livelihood',
            name='photo',
            field=models.ImageField(upload_to='gallery/livelihood'),
        ),
        migrations.AlterField(
            model_name='medical_camps',
            name='photo',
            field=models.ImageField(upload_to='gallery/medical_camps'),
        ),
        migrations.AlterField(
            model_name='women_empowerment',
            name='photo',
            field=models.ImageField(upload_to='gallery/women_empowerment'),
        ),
    ]
