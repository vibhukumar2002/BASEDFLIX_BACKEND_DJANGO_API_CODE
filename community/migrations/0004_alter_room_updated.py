# Generated by Django 5.0.1 on 2024-01-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
