# Generated by Django 5.0.4 on 2024-05-13 23:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0006_remove_room_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='Foto',
            field=models.ImageField(default=datetime.datetime(2024, 5, 13, 23, 33, 4, 108190, tzinfo=datetime.timezone.utc), upload_to=''),
            preserve_default=False,
        ),
    ]