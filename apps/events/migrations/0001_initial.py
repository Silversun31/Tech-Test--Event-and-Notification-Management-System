# Generated by Django 5.1.6 on 2025-02-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("location", models.CharField(max_length=255)),
                ("start_datetime", models.DateTimeField()),
                ("end_datetime", models.DateTimeField()),
            ],
            options={
                "ordering": ["start_datetime"],
            },
        ),
    ]
