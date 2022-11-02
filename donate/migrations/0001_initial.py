# Generated by Django 4.1.2 on 2022-11-02 09:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donate_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phn_no', models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(10)])),
                ('pan_no', models.IntegerField(validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)])),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.IntegerField()),
                ('purpose', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Give_Your_Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='payment_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_no', models.IntegerField(validators=[django.core.validators.MinLengthValidator(16), django.core.validators.MaxLengthValidator(16)])),
                ('ccv', models.IntegerField(validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(3)])),
                ('exp_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='payment_method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_using', models.IntegerField(choices=[(0, 'Card Payment'), (1, 'Internet Banking'), (2, 'UPI & E-Wallet'), (3, 'Other Payment Methods')], default=0)),
            ],
        ),
    ]
