# Generated by Django 4.0.4 on 2022-05-15 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/images/avatars/', verbose_name='profile picture'),
        ),
    ]