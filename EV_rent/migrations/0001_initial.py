# Generated by Django 4.1.6 on 2023-03-24 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("car_brand", models.CharField(max_length=50)),
                ("model", models.CharField(max_length=50)),
                ("charge_type", models.CharField(max_length=100)),
                ("horse_power", models.IntegerField()),
                ("num_sits", models.IntegerField()),
                ("range_km", models.IntegerField()),
                ("rent_price", models.FloatField()),
                ("year", models.IntegerField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="image_cars"),
                ),
                ("description", models.TextField()),
                ("url_page", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="RentalRequest",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("car_model", models.CharField(max_length=100)),
                ("num_days", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="ServiceRequest",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("car_model", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "photos",
                    models.ImageField(blank=True, upload_to="repair_images/%Y/%m/%d/"),
                ),
            ],
        ),
    ]
