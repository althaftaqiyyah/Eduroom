# Generated by Django 5.0.4 on 2024-05-31 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_remove_user_id_alter_user_nim'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default=datetime.datetime(2024, 5, 31, 15, 23, 38, 730767, tzinfo=datetime.timezone.utc), upload_to='profile'),
            preserve_default=False,
        ),
    ]
