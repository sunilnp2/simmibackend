# Generated by Django 4.1.2 on 2022-10-23 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latestnews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestnews',
            name='image',
            field=models.ImageField(blank=True, upload_to='latestnews'),
        ),
    ]
