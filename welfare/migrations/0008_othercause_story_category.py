# Generated by Django 4.1.2 on 2022-12-15 22:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welfare', '0007_remove_story_category_quote_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherCause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='welfare/other-causes')),
                ('date', models.DateField(default=datetime.date(2022, 12, 15))),
                ('category', models.CharField(choices=[('Drug Rehabilitation', 'Drug Rehabilitation'), ('Elder Healthcare', 'Elder Healthcare'), ('Environment Protection', 'Environment Protection'), ('Disaster Management', 'Disaster Management')], default='Drug Rehabilitation', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='story',
            name='category',
            field=models.CharField(choices=[('Education', 'EDUCATION'), ('HealthCare', 'HEALTHCARE'), ('Livelihood', 'LIVELIHOOD'), ('Women Empowerment', 'WOMEN EMPOWERMENT'), ('Others', 'OTHERS')], default='Education', max_length=20),
        ),
    ]