# Generated by Django 4.1.6 on 2023-03-25 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EV_rent", "0003_car_is_broken"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="is_rented",
            field=models.BooleanField(default=False),
        ),
    ]
