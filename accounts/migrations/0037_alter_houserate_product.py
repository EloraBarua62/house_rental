# Generated by Django 3.2.9 on 2022-03-10 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_remove_housedetails_house_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houserate',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.housedetails'),
        ),
    ]
