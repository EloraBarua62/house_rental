# Generated by Django 3.2.9 on 2021-12-04 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_housedetails_parking_lot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housedetails',
            name='house_id',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='House ID'),
        ),
    ]