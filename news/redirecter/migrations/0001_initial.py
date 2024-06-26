# Generated by Django 4.2 on 2023-04-08 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=150)),
                ('imgLink', models.CharField(max_length=150)),
                ('isForAdults', models.BooleanField(default=False)),
                ('isForeignNews', models.BooleanField(default=False)),
                ('tags', models.CharField(max_length=200)),
            ],
        ),
    ]
