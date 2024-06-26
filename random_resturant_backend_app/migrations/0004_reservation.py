# Generated by Django 4.2.13 on 2024-05-23 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("random_resturant_backend_app", "0003_product_delete_cartitem_delete_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservation",
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
                ("email", models.EmailField(max_length=254)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("party_size", models.IntegerField()),
                ("special_request", models.TextField()),
            ],
        ),
    ]
