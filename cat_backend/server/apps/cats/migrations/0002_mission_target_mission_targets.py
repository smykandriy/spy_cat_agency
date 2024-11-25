# Generated by Django 5.1.3 on 2024-11-25 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cats", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mission",
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
                ("complete", models.BooleanField(default=False)),
                (
                    "cat",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assigned_missions",
                        to="cats.spycat",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Target",
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
                ("name", models.CharField()),
                ("country", models.CharField()),
                ("notes", models.TextField(blank=True)),
                ("complete", models.BooleanField(default=False)),
                (
                    "mission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assigned_targets",
                        to="cats.mission",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="mission",
            name="targets",
            field=models.ManyToManyField(related_name="missions", to="cats.target"),
        ),
    ]