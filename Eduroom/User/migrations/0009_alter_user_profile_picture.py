# Generated by Django 5.0.4 on 2024-06-09 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='/profile_pictures/profile.png', upload_to='profile_pictures/'),
        ),
    ]
