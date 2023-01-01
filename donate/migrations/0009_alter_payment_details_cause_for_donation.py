# Generated by Django 4.1.2 on 2023-01-01 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0008_alter_payment_details_cause_for_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_details',
            name='cause_for_donation',
            field=models.CharField(choices=[('HealthCare', 'HealthCare'), ('Education', 'Education'), ('Livlihood', 'Livlihood'), ('Women Empowerment', 'Women Empowerment'), ('Other', 'Other')], max_length=100),
        ),
    ]
