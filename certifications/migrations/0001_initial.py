# Generated by Django 4.1.2 on 2022-12-03 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='certfication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('mentor_name', models.CharField(max_length=25)),
                ('issue_date', models.DateField()),
                ('img', models.FileField(upload_to='certificate')),
                ('status', models.CharField(choices=[('Not Completed', 'Not Completed'), ('Completed', 'Completed')], max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_certs', to='certifications.certfication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
