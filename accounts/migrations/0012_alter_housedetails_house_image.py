# Generated by Django 3.2.9 on 2021-12-17 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_housedetails_house_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housedetails',
            name='house_image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/', verbose_name='Add House Image'),
        ),
    ]
