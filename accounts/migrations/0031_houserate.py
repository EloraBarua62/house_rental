# Generated by Django 3.2.9 on 2022-03-04 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_housedetails_house_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_review', models.TextField()),
                ('info_rate', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=100)),
                ('infor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.housedetails')),
            ],
        ),
    ]
