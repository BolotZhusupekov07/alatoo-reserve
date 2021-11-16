from django.db import models
from django.db.models.signals import pre_save, pre_delete, post_save
from django.conf import settings
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from datetime import timedelta, datetime


class Category(models.Model):
    name = models.CharField(_("Название"), max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Категория зоны для брони")
        verbose_name_plural = _("Категории зон для брони")


class Place(models.Model):
    name = models.CharField(_("Название"), max_length=250, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, verbose_name=_("Категория")
    )
    rent_from = models.TimeField(_("Бронировать начиная"))
    rent_to = models.TimeField(_("Бронировать до"))
    interval = models.IntegerField(_("Интервал"))
    slug = models.SlugField(blank=True)
    only_administrators = models.BooleanField(
        _("Только админы"), default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Зона брони"
        verbose_name_plural = "Зоны брони"


class PlaceAdministrator(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, verbose_name="Зона брони"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )

    def __str__(self):
        return f"{self.user} - {self.place}"

    class Meta:
        verbose_name = "Администратор зоны"
        verbose_name_plural = "Aдминистратор зон"


@receiver(pre_save, sender=Place)
def set_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)


@receiver(post_save, sender=Place)
def create_time_periods(sender, instance, *args, **kwargs):
    rent_from = datetime.strptime(str(instance.rent_from), "%H:%M:%S")
    rent_to = datetime.strptime(str(instance.rent_to), "%H:%M:%S")
    while True:
        PlaceReservePeriod.objects.create(
            place=instance,
            starting_time=rent_from,
            finishing_time=rent_from + timedelta(minutes=instance.interval),
        )
        if rent_from + timedelta(minutes=instance.interval) >= rent_to:
            f = rent_from + (rent_to - rent_from)
            PlaceReservePeriod.objects.create(
                place=instance, starting_time=rent_from, finishing_time=f
            )
            break
        rent_from = rent_from + timedelta(minutes=instance.interval)


class PlaceReservePeriod(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, verbose_name="Зона брони"
    )
    starting_time = models.TimeField(_("Начало"))
    finishing_time = models.TimeField(_("Конец"))

    class Meta:
        verbose_name = _("Период брони")
        verbose_name_plural = _("Периоды брони")

    def __str__(self):
        return f"{self.place}: {self.starting_time} - {self.finishing_time}"


class Reserve(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    reserve_period = models.ForeignKey(
        PlaceReservePeriod,
        on_delete=models.CASCADE,
        verbose_name="Период брони",
    )
    date = models.DateField(_("Дата"))
    reason = models.CharField(_("Причина"), max_length=200)

    class Meta:
        verbose_name = _("Бронь")
        verbose_name_plural = _("Брони")

    def __str__(self):
        return f"{self.user.email} - {self.reserve_period} - {self.reason}"
