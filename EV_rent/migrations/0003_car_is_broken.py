# Generated by Django 4.1.6 on 2023-03-24 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EV_rent", "0002_rentalrequest_is_broken"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="is_broken",
            field=models.BooleanField(default=False),
        ),
    ]
