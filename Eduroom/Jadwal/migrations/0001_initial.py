# Generated by Django 5.0.4 on 2024-04-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idRuangan', models.CharField(max_length=100)),
                ('waktu', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
