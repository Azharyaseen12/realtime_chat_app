# Generated by Django 4.2.6 on 2024-05-04 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_id_alter_room_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
