# Generated by Django 5.0.4 on 2024-05-31 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_remove_user_no_handphone_remove_user_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='NIM',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
