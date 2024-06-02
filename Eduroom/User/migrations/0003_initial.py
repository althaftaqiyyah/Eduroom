# Generated by Django 5.0.4 on 2024-04-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0002_delete_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=100)),
                ('Nama', models.CharField(max_length=100)),
                ('NIM', models.CharField(max_length=100)),
                ('departemen', models.CharField(max_length=100)),
                ('No_handphone', models.CharField(max_length=100)),
            ],
        ),
    ]