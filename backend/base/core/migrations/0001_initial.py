# Generated by Django 2.2.24 on 2021-09-16 18:12

import core.db
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_update', core.db.AutoDateTimeField(default=django.utils.timezone.now)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('name', models.CharField(max_length=500, null=True, verbose_name='Nome')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=150, unique=True, verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('phone', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('country_code_number', models.IntegerField(choices=[(1, '+1'), (55, '+55'), (52, '+52')], null=True)),
                ('password', models.CharField(max_length=128, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('access_attempts_number', models.SmallIntegerField(blank=True, null=True)),
                ('is_blocked', models.BooleanField(default=False)),
                ('bypass', models.BooleanField(default=False)),
                ('preferred_language', models.IntegerField(choices=[(1, 'ENGLISH'), (2, 'PORTUGUES'), (3, 'ESPANOL')], default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('registration_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MessageTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_update', core.db.AutoDateTimeField(default=django.utils.timezone.now)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('path', models.CharField(max_length=255, unique=True)),
                ('template', models.TextField()),
                ('type', models.IntegerField(choices=[(1, 'EMAIL'), (2, 'SMS')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserSequence',
            fields=[
                ('sequence', models.AutoField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageLogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_update', core.db.AutoDateTimeField(default=django.utils.timezone.now)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('sent', models.DateTimeField(blank=True, null=True)),
                ('scheduled', models.DateTimeField(blank=True, null=True)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('recipient', models.CharField(blank=True, max_length=255, null=True)),
                ('related_entity_uuid', models.UUIDField(null=True)),
                ('message_template', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.MessageTemplate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]