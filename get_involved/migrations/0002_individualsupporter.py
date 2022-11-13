# Generated by Django 4.1.2 on 2022-11-14 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_involved', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualSupporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('reason', models.TextField()),
                ('timing', models.DateField()),
                ('message', models.TextField()),
                ('file', models.FileField(blank=True, upload_to='supporter')),
            ],
        ),
    ]
