# Generated by Django 4.1.2 on 2022-12-09 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0002_remove_payment_details_card_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_details',
            name='cause_for_donation',
            field=models.CharField(choices=[('Education', 'Education'), ('Medical camps', 'Medical camps'), ('Livelihood', 'Livelihood'), ('Women empowerment', 'Women empowerment'), ('Healthcare', 'Healthcare')], max_length=100),
        ),
    ]
