# Generated by Django 4.1.2 on 2022-12-13 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0006_alter_payment_details_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_details',
            name='cause_for_donation',
            field=models.CharField(choices=[('Other', 'Other'), ('Livlihood', 'Livlihood'), ('Women Empowerment', 'Women Empowerment'), ('Education', 'Education'), ('HealthCare', 'HealthCare')], max_length=100),
        ),
    ]