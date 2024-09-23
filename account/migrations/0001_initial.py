# Generated by Django 5.1.1 on 2024-09-23 20:48

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('phone_number', models.CharField(blank=True, max_length=12, verbose_name='phone number')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='user name')),
                ('address', models.CharField(blank=True, max_length=255)),
                ('first_name', models.CharField(blank=True, max_length=64, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=64, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', account.models.CustomeUserManager()),
            ],
        ),
    ]
