# Generated by Django 4.0.4 on 2022-05-10 05:40

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_store_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='category',
            field=models.CharField(choices=[('SUPERMARKET', 'SUPERMARKET'), ('GROCER_STORE', 'GROCER STORE'), ('BUTCHER', 'BUTCHER'), ('BAKER', 'BAKER'), ('FISHMONGER', 'FISH MONGER'), ('CHEMIST', 'CHEMIST or PHAMARCY'), ('FASHION', 'FASHION'), ('BOOK_SHOP', 'BOOK SHOP'), ('HAIRDRESSER|BARBER', 'HAIRDRESSER & BARBER'), ('PATROL_STATION', 'PATROL STATION'), ('OTHERS', 'OTHERS')], default='FASHION', max_length=255, verbose_name='Choose your category'),
        ),
        migrations.AlterField(
            model_name='store',
            name='location',
            field=location_field.models.plain.PlainLocationField(blank=True, max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Store name'),
        ),
        migrations.AlterField(
            model_name='store',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, max_length=255, verbose_name='Amount'),
        ),
    ]
