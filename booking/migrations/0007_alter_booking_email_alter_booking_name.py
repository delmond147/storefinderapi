# Generated by Django 4.0.4 on 2022-05-10 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_remove_booking_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='', max_length=255, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='username'),
        ),
    ]
