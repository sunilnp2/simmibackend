# Generated by Django 4.1.2 on 2022-11-28 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate_certificate', '0002_donationcetificates'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationcetificates',
            name='transactions_type',
            field=models.CharField(default='Donation', max_length=30),
        ),
    ]