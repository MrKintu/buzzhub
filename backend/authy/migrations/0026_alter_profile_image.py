# Generated by Django 4.2.7 on 2023-11-25 19:03

import authy.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authy", "0025_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(null=True, upload_to=authy.models.rename_image),
        ),
    ]