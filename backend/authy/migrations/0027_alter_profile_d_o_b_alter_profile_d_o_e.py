# Generated by Django 4.2.7 on 2023-12-03 09:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authy", "0026_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="d_o_b",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="d_o_e",
            field=models.DateField(blank=True, null=True),
        ),
    ]
