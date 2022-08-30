# Generated by Django 4.1 on 2022-08-30 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0012_cart_order_cartproduct"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description_ar",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="policy_return",
            field=models.CharField(default="", max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="policy_return_ar",
            field=models.CharField(default="", max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="title_ar",
            field=models.CharField(default="", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="warnty",
            field=models.CharField(default="", max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="warnty_ar",
            field=models.CharField(default="", max_length=250),
            preserve_default=False,
        ),
    ]