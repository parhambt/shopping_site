# Generated by Django 5.1 on 2024-09-21 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0004_remove_cartitem_json_variation"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="json",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
