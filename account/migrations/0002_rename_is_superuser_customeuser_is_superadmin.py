# Generated by Django 5.1.1 on 2024-09-23 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeuser',
            old_name='is_superuser',
            new_name='is_superadmin',
        ),
    ]
