# Generated by Django 4.1.6 on 2023-03-30 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("EV_rent", "0019_remove_servicerequest_email_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="servicerequest", name="description_en",),
        migrations.RemoveField(model_name="servicerequest", name="description_ru",),
    ]
