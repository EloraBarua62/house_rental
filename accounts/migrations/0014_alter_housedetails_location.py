# Generated by Django 4.0 on 2021-12-22 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_housedetails_house_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housedetails',
            name='location',
            field=models.TextField(blank=True, max_length=250, verbose_name='Location'),
        ),
    ]
