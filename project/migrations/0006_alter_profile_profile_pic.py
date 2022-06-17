# Generated by Django 3.2 on 2022-06-17 06:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20220617_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='cld-sample', max_length=255, verbose_name='image'),
        ),
    ]
