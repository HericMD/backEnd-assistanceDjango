# Generated by Django 4.2.4 on 2023-08-04 04:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ["-date_joined"],
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
        ),
    ]