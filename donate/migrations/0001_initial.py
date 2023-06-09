# Generated by Django 4.1.2 on 2023-01-01 14:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
                ('subscription_plan', models.CharField(max_length=100)),
                ('cause_for_donation', models.CharField(choices=[('Education', 'Education'), ('Women Empowerment', 'Women Empowerment'), ('Livlihood', 'Livlihood'), ('HealthCare', 'HealthCare'), ('Other', 'Other')], max_length=100)),
                ('amount_type', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=9999999)),
                ('fname', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('country_code', models.CharField(max_length=10)),
                ('num', models.CharField(max_length=18)),
                ('country', models.CharField(max_length=25)),
                ('desc', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='payment_method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_using', models.IntegerField(choices=[(0, 'Card Payment'), (1, 'Internet Banking'), (2, 'UPI & E-Wallet'), (3, 'Other Payment Methods')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='upi_tran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('paas', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(8)])),
            ],
        ),
        migrations.CreateModel(
            name='donate_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phn_no', models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(10)])),
                ('pan_no', models.IntegerField(validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)])),
                ('address', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.IntegerField()),
                ('purpose', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
