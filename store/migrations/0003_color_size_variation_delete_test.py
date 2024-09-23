# Generated by Django 5.1 on 2024-09-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_test"),
    ]

    operations = [
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("color", models.CharField(max_length=20, unique=True)),
                (
                    "numeric_color",
                    models.CharField(blank=True, max_length=7, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Size",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("size", models.CharField(max_length=20, unique=True)),
                ("numeric_size", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Variation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("colors", models.ManyToManyField(to="store.color")),
                ("sizes", models.ManyToManyField(to="store.size")),
            ],
        ),
        migrations.DeleteModel(
            name="Test",
        ),
    ]
