# Generated by Django 3.2.9 on 2022-03-05 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_houserate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
