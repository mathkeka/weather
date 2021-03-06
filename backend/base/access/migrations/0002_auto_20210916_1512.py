# Generated by Django 2.2.24 on 2021-09-16 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enablement',
            name='registration_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='enablement_registration_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='enablement',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='enablement_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='profilefunctionality',
            unique_together={('functionality', 'profile')},
        ),
        migrations.AlterUniqueTogether(
            name='managementprofile',
            unique_together={('profile_manager', 'profile_managed')},
        ),
    ]
