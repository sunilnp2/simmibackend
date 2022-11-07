# Generated by Django 4.1.2 on 2022-11-07 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_description', models.TextField()),
                ('speaker_name', models.CharField(max_length=50)),
                ('Perk_of_attendig_event', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='events')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='events/extra_images')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]
