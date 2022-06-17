# Generated by Django 3.2 on 2022-06-17 06:16

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dkz8w5n6k/image/upload/v1655118797/qrzikn4v4wjqoebq0tfh.jpg', max_length=255, verbose_name='image'),
        ),
    ]