# Generated by Django 4.1.6 on 2023-03-30 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("EV_rent", "0016_car_car_full_name_alter_rentalrequest_car_model_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rentalrequest", old_name="email", new_name="person",
        ),
        migrations.RemoveField(model_name="rentalrequest", name="first_name",),
        migrations.RemoveField(model_name="rentalrequest", name="last_name",),
    ]
