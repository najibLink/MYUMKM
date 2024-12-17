# Generated by Django 5.1.3 on 2024-12-04 01:48

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelanggan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pelanggan', models.CharField(max_length=100)),
                ('alamat_pelanggan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Penjualan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_penjualan', models.DateField()),
                ('jumlah_terjual', models.PositiveIntegerField()),
                ('total_harga', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_produk', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Tersedia', 'Tersedia'), ('Tidak Tersedia', 'Tidak Tersedia')], max_length=50)),
                ('kategori', models.CharField(max_length=100)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stok', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('status_pembayaran', models.CharField(choices=[('LUNAS', 'Lunas'), ('BELUM_LUNAS', 'Belum Lunas'), ('MENUNGGU', 'Menunggu Pembayaran')], default='MENUNGGU', max_length=20)),
                ('metode', models.CharField(choices=[('TRANSFER', 'Transfer Bank'), ('TUNAI', 'Tunai'), ('KARTU', 'Kartu Kredit/Debit'), ('EWALLET', 'E-Wallet')], max_length=20)),
                ('idPelanggan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pembayarans', to='umkmapp.pelanggan')),
                ('idPenjualan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pembayarans', to='umkmapp.penjualan')),
            ],
        ),
        migrations.AddField(
            model_name='penjualan',
            name='idProduk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='penjualans', to='umkmapp.produk'),
        ),
        migrations.CreateModel(
            name='Pengiriman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_pengiriman', models.DateField()),
                ('estimasi', models.CharField(max_length=50)),
                ('idPelanggan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pengirimans', to='umkmapp.pelanggan')),
                ('produk', models.ManyToManyField(blank=True, related_name='pengirimans', to='umkmapp.produk')),
            ],
        ),
        migrations.AddField(
            model_name='pelanggan',
            name='produk_dibeli',
            field=models.ManyToManyField(blank=True, related_name='pelanggans', to='umkmapp.produk'),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_supplier', models.CharField(max_length=100)),
                ('alamat_supplier', models.TextField()),
                ('idProduk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='umkmapp.produk')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='umkmapp_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='umkmapp_user_permissions_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='produk',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='umkmapp.user'),
        ),
        migrations.CreateModel(
            name='Pendapatan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periode', models.CharField(max_length=50)),
                ('total_pendapatan', models.DecimalField(decimal_places=2, max_digits=15)),
                ('id_pembayaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pendapatans', to='umkmapp.pembayaran')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pendapatans', to='umkmapp.user')),
            ],
        ),
    ]
