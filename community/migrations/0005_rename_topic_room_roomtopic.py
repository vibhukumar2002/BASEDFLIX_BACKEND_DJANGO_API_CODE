# Generated by Django 5.0.1 on 2024-01-09 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_alter_room_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='topic',
            new_name='roomtopic',
        ),
    ]
