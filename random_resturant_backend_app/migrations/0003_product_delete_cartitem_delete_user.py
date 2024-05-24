# Generated by Django 4.2.13 on 2024-05-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("random_resturant_backend_app", "0002_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="CartItem",
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
