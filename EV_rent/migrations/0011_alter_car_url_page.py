# Generated by Django 4.1.6 on 2023-03-28 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EV_rent", "0010_caryear_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car", name="url_page", field=models.SlugField(unique=True),
        ),
    ]
