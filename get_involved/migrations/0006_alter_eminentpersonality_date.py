# Generated by Django 4.1.2 on 2022-11-25 22:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('get_involved', '0005_eminentpersonality_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eminentpersonality',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
