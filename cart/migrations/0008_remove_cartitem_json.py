# Generated by Django 5.1 on 2024-09-21 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0007_cartitem_json"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="json",
        ),
    ]
