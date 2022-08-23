# Generated by Django 4.1 on 2022-08-20 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0005_slider"),
    ]

    operations = [
        migrations.CreateModel(
            name="Offer",
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
                ("title", models.CharField(max_length=250)),
                ("rate", models.IntegerField(default=0)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="offer/")),
            ],
        ),
    ]