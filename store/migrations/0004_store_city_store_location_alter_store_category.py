# Generated by Django 4.0.3 on 2022-04-14 12:51

from django.db import migrations, models
import django.utils.timezone
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_store_description_alter_store_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='Mambanda', max_length=63),
        ),
        migrations.AlterField(
            model_name='store',
            name='category',
            field=models.CharField(choices=[('DEPARTMENT_STORE', 'DEPARTMENT STORE'), ('SUPERMARKET', 'SUPERMARKET'), ('BUTCHER', 'BUTCHER'), ('BAKER', 'BAKER'), ('CHEMIST', 'CHEMIST'), ('JEWELLERY_STORE', 'JEWELLERY STORE'), ('SHOE_SHOP', 'SHOE SHOP'), ('HAIRDRESSER|BARBER', 'HAIRDRESSER|BARBER'), ('PATROL_STATION', 'PATROL_STATION'), ('TEA_SHOP', 'TEA_SHOP'), ('OTHERS', 'OTHERS')], default='SUPERMARKET', max_length=255),
        ),
    ]
