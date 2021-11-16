# Generated by Django 3.2.8 on 2021-11-16 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(max_length=150, verbose_name="Название"),
                ),
            ],
            options={
                "verbose_name": "Категория зоны для брони",
                "verbose_name_plural": "Категории зон для брони",
            },
        ),
        migrations.CreateModel(
            name="Place",
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
                (
                    "name",
                    models.CharField(
                        max_length=250, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "rent_from",
                    models.TimeField(verbose_name="Бронировать начиная"),
                ),
                ("rent_to", models.TimeField(verbose_name="Бронировать до")),
                ("interval", models.IntegerField(verbose_name="Интервал")),
                ("slug", models.SlugField(blank=True)),
                (
                    "only_administrators",
                    models.BooleanField(
                        default=False, verbose_name="Только админы"
                    ),
                ),
            ],
            options={
                "verbose_name": "Зона брони",
                "verbose_name_plural": "Зоны брони",
            },
        ),
        migrations.CreateModel(
            name="PlaceAdministrator",
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
            ],
            options={
                "verbose_name": "Администратор зоны",
                "verbose_name_plural": "Aдминистратор зон",
            },
        ),
        migrations.CreateModel(
            name="PlaceReservePeriod",
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
                ("starting_time", models.TimeField(verbose_name="Начало")),
                ("finishing_time", models.TimeField(verbose_name="Конец")),
            ],
            options={
                "verbose_name": "Период брони",
                "verbose_name_plural": "Периоды брони",
            },
        ),
        migrations.CreateModel(
            name="Reserve",
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
                ("date", models.DateField(verbose_name="Дата")),
                (
                    "reason",
                    models.CharField(max_length=200, verbose_name="Причина"),
                ),
                (
                    "reserve_period",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reserve.placereserveperiod",
                        verbose_name="Период брони",
                    ),
                ),
            ],
            options={
                "verbose_name": "Бронь",
                "verbose_name_plural": "Брони",
            },
        ),
    ]