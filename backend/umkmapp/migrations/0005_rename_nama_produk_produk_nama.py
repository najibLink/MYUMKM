# Generated by Django 5.1.3 on 2024-12-16 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umkmapp', '0004_alter_produk_gambar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produk',
            old_name='nama_produk',
            new_name='nama',
        ),
    ]