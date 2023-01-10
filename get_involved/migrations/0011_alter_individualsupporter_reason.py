# Generated by Django 4.1.2 on 2023-01-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_involved', '0010_alter_individualsupporter_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualsupporter',
            name='reason',
            field=models.CharField(choices=[('Education', 'Education'), ('Women Empowerment', 'Women Empowerment'), ('Livelihood', 'Livelihood'), ('Other', 'Other'), ('Healthcare', 'Healthcare')], max_length=100),
        ),
    ]