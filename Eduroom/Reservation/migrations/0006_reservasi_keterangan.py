# Generated by Django 5.0.4 on 2024-05-10 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0005_reservasi_nama_peminjam'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservasi',
            name='Keterangan',
            field=models.CharField(default=datetime.datetime(2024, 5, 10, 8, 34, 17, 741442, tzinfo=datetime.timezone.utc), max_length=500),
            preserve_default=False,
        ),
    ]
