# Generated by Django 4.1.2 on 2022-10-29 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_transactions',
            name='amount',
            field=models.IntegerField(default=100),
        ),
    ]