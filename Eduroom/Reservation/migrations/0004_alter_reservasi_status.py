# Generated by Django 5.0.4 on 2024-05-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0003_reservasi_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservasi',
            name='status',
            field=models.CharField(choices=[('Kosong', 'Kosong'), ('Dalam proses', 'Dalam proses'), ('Diterima', 'Diterima'), ('Ditolak', 'Ditolak')], default='---', max_length=20),
        ),
    ]
