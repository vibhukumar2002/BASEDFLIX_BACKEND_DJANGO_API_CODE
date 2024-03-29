# Generated by Django 5.0.1 on 2024-01-12 10:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_message_reply'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated']},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['-updated']},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated']},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-updated']},
        ),
        migrations.CreateModel(
            name='favs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieid', models.IntegerField(unique=True)),
                ('moviename', models.CharField(max_length=300)),
                ('dateadded', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['dateadded'],
            },
        ),
    ]
