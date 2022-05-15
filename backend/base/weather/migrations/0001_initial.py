# Generated by Django 2.2.28 on 2022-05-15 18:18

import core.db
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
    ]