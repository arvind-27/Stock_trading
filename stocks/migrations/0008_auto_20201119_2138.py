# Generated by Django 3.1.3 on 2020-11-19 21:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks', '0007_delete_useraccountcurrentvalue'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAccountValue',
            new_name='AccountValue',
        ),
    ]
