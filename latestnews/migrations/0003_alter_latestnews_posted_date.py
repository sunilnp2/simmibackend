# Generated by Django 4.1.2 on 2022-10-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latestnews', '0002_alter_latestnews_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestnews',
            name='posted_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]