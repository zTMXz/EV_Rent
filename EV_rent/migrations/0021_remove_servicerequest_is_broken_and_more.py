# Generated by Django 4.1.6 on 2023-03-30 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("EV_rent", "0020_remove_servicerequest_description_en_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="servicerequest", name="is_broken",),
        migrations.RemoveField(model_name="servicerequest", name="is_rented",),
    ]
