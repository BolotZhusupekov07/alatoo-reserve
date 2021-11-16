from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")
        if other_fields.get("is_active") is not True:
            raise ValueError("Superuser must be assigned to is_active=True")
        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError(_("You must provide an email"))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Почта"), unique=True)
    creation_date = models.DateTimeField(_("Создано"), auto_now_add=True)
    is_staff = models.BooleanField(_("Админ"), default=False)
    is_active = models.BooleanField(_("Активный"), default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):

        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
