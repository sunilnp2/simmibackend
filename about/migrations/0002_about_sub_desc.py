# Generated by Django 4.1.2 on 2022-11-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='sub_desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
