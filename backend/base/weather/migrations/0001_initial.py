# Generated by Django 2.2.28 on 2022-05-16 01:39

import core.db
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_update', core.db.AutoDateTimeField(default=django.utils.timezone.now)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('woeid', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('results', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_update', core.db.AutoDateTimeField(default=django.utils.timezone.now)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('year', models.IntegerField()),
                ('date', models.CharField(max_length=5)),
                ('weekday', models.CharField(max_length=10)),
                ('max', models.IntegerField()),
                ('min', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=20)),
                ('weather', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='weather.Weather')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FavoriteForecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_update', core.db.AutoDateTimeField(default=django.utils.timezone.now)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('forecast', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='weather.Forecast')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='favorite_weather_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
