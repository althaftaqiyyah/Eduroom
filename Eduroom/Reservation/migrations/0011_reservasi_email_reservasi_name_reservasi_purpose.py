# Generated by Django 5.0.4 on 2024-06-08 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0010_alter_reservasi_waktu_mulai_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservasi',
            name='Email',
            field=models.EmailField(default=datetime.datetime(2024, 6, 8, 17, 27, 51, 324971, tzinfo=datetime.timezone.utc), max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservasi',
            name='Name',
            field=models.CharField(default=datetime.datetime(2024, 6, 8, 17, 27, 59, 837422, tzinfo=datetime.timezone.utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservasi',
            name='Purpose',
            field=models.TextField(default=datetime.datetime(2024, 6, 8, 17, 28, 4, 151955, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
