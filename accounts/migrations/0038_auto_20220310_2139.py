# Generated by Django 3.2.9 on 2022-03-10 15:39

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_alter_houserate_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='housedetails',
            name='nid_back',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_image, verbose_name='NID back picture'),
        ),
        migrations.AddField(
            model_name='housedetails',
            name='nid_front',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_image, verbose_name='NID front picture'),
        ),
        migrations.AddField(
            model_name='housedetails',
            name='user_photo',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_image, verbose_name='User profile picture'),
        ),
    ]