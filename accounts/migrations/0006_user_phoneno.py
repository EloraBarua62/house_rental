# Generated by Django 3.2.9 on 2021-12-04 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_housedetails_house_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phoneno',
            field=models.CharField(blank=True, max_length=15, verbose_name='Phone No'),
        ),
    ]
