# Generated by Django 5.1.3 on 2024-11-26 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umkmapp', '0002_remove_user_nama'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254, unique=True),
        ),
    ]
