# Generated by Django 4.2 on 2023-10-16 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_productprices_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="productprices",
            name="name",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]