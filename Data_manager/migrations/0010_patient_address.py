# Generated by Django 5.0.6 on 2024-10-24 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_manager', '0009_rename_profile_created_on_patient_profile_created_on_or_first_diagnos'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.TextField(default='NA'),
            preserve_default=False,
        ),
    ]
