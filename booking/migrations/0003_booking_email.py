# Generated by Django 4.0.4 on 2022-04-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_remove_booking_payment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='', max_length=255),
        ),
    ]
