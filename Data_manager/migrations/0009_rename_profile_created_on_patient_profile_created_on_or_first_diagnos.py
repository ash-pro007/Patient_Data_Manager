# Generated by Django 5.0.6 on 2024-10-22 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Data_manager', '0008_patient_profile_created_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='profile_created_on',
            new_name='profile_created_on_or_first_diagnos',
        ),
    ]
