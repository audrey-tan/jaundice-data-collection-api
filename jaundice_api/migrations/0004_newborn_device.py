# Generated by Django 4.2.13 on 2024-07-04 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jaundice_api", "0003_alter_imagemodel_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="newborn",
            name="device",
            field=models.CharField(default=" ", max_length=256),
            preserve_default=False,
        ),
    ]
