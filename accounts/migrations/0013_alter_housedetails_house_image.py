# Generated by Django 3.2.9 on 2021-12-17 19:16

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_housedetails_house_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housedetails',
            name='house_image',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_image, verbose_name='Add House Image'),
        ),
    ]
