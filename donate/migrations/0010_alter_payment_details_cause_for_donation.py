# Generated by Django 4.1.2 on 2022-12-15 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0009_alter_payment_details_cause_for_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_details',
            name='cause_for_donation',
            field=models.CharField(choices=[('Livlihood', 'Livlihood'), ('Women Empowerment', 'Women Empowerment'), ('HealthCare', 'HealthCare'), ('Education', 'Education'), ('Other', 'Other')], max_length=100),
        ),
    ]
