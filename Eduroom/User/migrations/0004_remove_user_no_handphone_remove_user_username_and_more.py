# Generated by Django 5.0.4 on 2024-05-27 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='No_handphone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='departemen',
        ),
    ]
