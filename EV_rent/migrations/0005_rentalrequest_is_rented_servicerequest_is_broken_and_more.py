# Generated by Django 4.1.6 on 2023-03-25 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EV_rent", "0004_car_is_rented"),
    ]

    operations = [
        migrations.AddField(
            model_name="rentalrequest",
            name="is_rented",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="servicerequest",
            name="is_broken",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="servicerequest",
            name="is_rented",
            field=models.BooleanField(default=False),
        ),
    ]
