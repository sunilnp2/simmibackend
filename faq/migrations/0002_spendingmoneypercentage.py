# Generated by Django 4.1.2 on 2022-12-26 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpendingMoneyPercentage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=10)),
                ('healthcare', models.CharField(max_length=10)),
                ('livelyhood', models.CharField(max_length=10)),
                ('women_empowerment', models.CharField(max_length=10)),
                ('other', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
