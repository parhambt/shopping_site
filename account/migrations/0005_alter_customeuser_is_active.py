# Generated by Django 5.1.1 on 2024-09-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_customeuser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
