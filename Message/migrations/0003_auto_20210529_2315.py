# Generated by Django 3.1.7 on 2021-05-29 20:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Message', '0002_message_readconf'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Messages',
        ),
    ]
