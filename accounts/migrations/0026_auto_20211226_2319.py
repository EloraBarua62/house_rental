# Generated by Django 3.2.9 on 2021-12-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_remove_housedetails_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='housedetails',
            name='home',
            field=models.CharField(blank=True, max_length=50, verbose_name='House Name'),
        ),
        migrations.AddField(
            model_name='housedetails',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Rent'),
        ),
        migrations.AlterField(
            model_name='housedetails',
            name='house_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='House ID'),
        ),
        migrations.AlterField(
            model_name='housedetails',
            name='location',
            field=models.CharField(blank=True, max_length=250, verbose_name='Location'),
        ),
    ]
