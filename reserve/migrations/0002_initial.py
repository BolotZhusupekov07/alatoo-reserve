# Generated by Django 3.2.8 on 2021-11-16 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("reserve", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="reserve",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="placereserveperiod",
            name="place",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="reserve.place",
                verbose_name="Зона брони",
            ),
        ),
        migrations.AddField(
            model_name="placeadministrator",
            name="place",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="reserve.place",
                verbose_name="Зона брони",
            ),
        ),
        migrations.AddField(
            model_name="placeadministrator",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="place",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="reserve.category",
                verbose_name="Категория",
            ),
        ),
    ]