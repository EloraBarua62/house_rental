# Generated by Django 3.2.9 on 2021-12-24 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_alter_housedetails_house_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housedetails',
            name='house_name',
        ),
    ]