# Generated by Django 5.0.6 on 2024-10-28 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Data_manager', '0015_alter_patient_treatment_images_treatment_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient_treatment_details',
            old_name='weigth',
            new_name='weight',
        ),
    ]
