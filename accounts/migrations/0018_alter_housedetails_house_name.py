# Generated by Django 3.2.9 on 2021-12-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_housedetails_house_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housedetails',
            name='house_name',
            field=models.CharField(blank=True, max_length=20, verbose_name='House Name'),
        ),
    ]
