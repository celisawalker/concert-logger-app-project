# Generated by Django 5.2.1 on 2025-06-02 23:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_library_alter_concert_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Library',
        ),
        migrations.AlterField(
            model_name='concert',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
