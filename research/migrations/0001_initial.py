# Generated by Django 4.1.2 on 2022-11-26 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('organization', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('how_we_helped', models.TextField()),
                ('year', models.IntegerField()),
                ('article_link', models.URLField()),
                ('image', models.ImageField(upload_to='research')),
            ],
        ),
    ]