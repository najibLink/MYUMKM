# Generated by Django 5.1.3 on 2024-11-26 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umkmapp', '0003_remove_user_username_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]