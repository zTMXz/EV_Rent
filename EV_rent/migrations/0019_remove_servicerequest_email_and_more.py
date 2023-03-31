# Generated by Django 4.1.6 on 2023-03-30 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("EV_rent", "0018_remove_rentalrequest_is_broken_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="servicerequest", name="email",),
        migrations.RemoveField(model_name="servicerequest", name="first_name",),
        migrations.RemoveField(model_name="servicerequest", name="last_name",),
        migrations.AddField(
            model_name="servicerequest",
            name="person",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="car",
            name="car_full_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="servicerequest",
            name="car_model",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="EV_rent.car"
            ),
        ),
    ]
