# Generated by Django 4.1.2 on 2022-12-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0005_alter_payment_details_cause_for_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_details',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
