# Generated by Django 4.1 on 2022-08-15 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("seoul_bike", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MonthUsage",
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
                ("month", models.CharField(blank=True, max_length=255, null=True)),
                ("bike_usage", models.BigIntegerField(blank=True, null=True)),
            ],
            options={"db_table": "month_usage", "managed": False,},
        ),
    ]
