# Generated by Django 4.1.2 on 2022-12-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tender_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='tender/')),
                ('contents', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Archived', 'Archived')], max_length=10)),
            ],
        ),
    ]
