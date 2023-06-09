# Generated by Django 4.1.2 on 2022-12-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Speaker name')),
                ('event', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('place', models.CharField(max_length=50)),
                ('speaker_profile', models.ImageField(blank=True, upload_to='events/speaker_profile')),
            ],
        ),
    ]
