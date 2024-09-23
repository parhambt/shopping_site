# Generated by Django 5.1 on 2024-09-22 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0009_cartitem_json_variation"),
        ("store", "0006_alter_variation_colors_alter_variation_sizes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="json_variation",
        ),
        migrations.AddField(
            model_name="cartitem",
            name="variation",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.variation",
            ),
        ),
    ]
