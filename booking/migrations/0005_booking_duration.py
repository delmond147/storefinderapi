# Generated by Django 4.0.4 on 2022-05-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_remove_booking_owner_booking_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='duration',
            field=models.DateField(auto_created=True, auto_now=True),
        ),
    ]