# Generated by Django 3.2.9 on 2021-12-24 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_housedetails_house_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='housedetails',
            old_name='house_name',
            new_name='name',
        ),
    ]