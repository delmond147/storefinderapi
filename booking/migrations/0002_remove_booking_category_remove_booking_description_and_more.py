# Generated by Django 4.0.3 on 2022-04-15 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_store_name_alter_store_category_alter_store_location'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='category',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='description',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='image',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='price',
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_type',
            field=models.CharField(choices=[('MOBILE MONEY', [('MTN', 'MTN'), ('ORANGE', 'Orange')]), ('BANK TRANSACTION', [('MASTER', 'Debit Card'), ('MASTER', 'Credit Card'), ('MASTER', 'Visa Card')]), ('CRYPTO CURRENCY', [('BITCOIN', 'Bitcoin'), ('PLANTICOIN', 'Planticoin')])], default='MTN', max_length=255),
        ),
        migrations.AlterField(
            model_name='booking',
            name='store',
            field=models.ForeignKey(default='SUPERMARKET', on_delete=django.db.models.deletion.CASCADE, to='store.store'),
        ),
    ]
