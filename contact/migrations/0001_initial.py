# Generated by Django 4.1.2 on 2022-10-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
    ]