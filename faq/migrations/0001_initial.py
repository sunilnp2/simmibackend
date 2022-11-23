# Generated by Django 4.1.2 on 2022-11-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quention', models.TextField(help_text='frequently asked question from user')),
                ('answer', models.TextField(help_text='answer')),
            ],
        ),
    ]
