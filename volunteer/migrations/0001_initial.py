# Generated by Django 4.1.2 on 2022-11-02 09:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(10)])),
                ('address', models.TextField()),
                ('aadhar_no', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(16)])),
                ('dob', models.DateField()),
                ('blood_group', models.CharField(max_length=10)),
            ],
        ),
    ]
