# Generated by Django 4.2.4 on 2023-08-19 19:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_topic_room_host_room_topic'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study_messages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
    ]
