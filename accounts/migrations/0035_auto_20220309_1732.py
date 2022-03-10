# Generated by Django 3.2.9 on 2022-03-09 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_alter_houserate_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houserate',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='houserate',
            name='rate',
        ),
        migrations.AddField(
            model_name='houserate',
            name='ip',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='houserate',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='houserate',
            name='review',
            field=models.TextField(blank=True, max_length=750),
        ),
        migrations.AddField(
            model_name='houserate',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='houserate',
            name='subject',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='houserate',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]