# Generated by Django 3.1.3 on 2020-11-15 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile_number',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='money',
            field=models.FloatField(default=100000.0),
        ),
        migrations.AddField(
            model_name='profile',
            name='pan',
            field=models.CharField(default='', max_length=10),
        ),
    ]