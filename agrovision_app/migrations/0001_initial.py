# Generated by Django 4.1.13 on 2024-04-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClimateData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('precipitation', models.FloatField()),
                ('temp_max', models.FloatField()),
                ('temp_min', models.FloatField()),
                ('wind', models.FloatField()),
                ('climate', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CropRecommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N', models.FloatField()),
                ('P', models.FloatField()),
                ('K', models.FloatField()),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('ph', models.FloatField()),
                ('rainfall', models.FloatField()),
                ('label', models.CharField(max_length=100)),
            ],
        ),
    ]
