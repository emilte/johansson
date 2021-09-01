# imports
import json

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Avg, Count, Min, Sum
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


# End: imports -----------------------------------------------------------------

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **kwargs):
        user = self.create_user(username=username, password=password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    GENDER_CHOICES = [
        (None, None),
        (MALE, "Mann"),
        (FEMALE, "Kvinne"),
        (OTHER, "Annet"),
    ]
    username = models.CharField(max_length=60, unique=True, verbose_name="brukernavn")
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=60, null=True, blank=True, verbose_name="fornavn")
    last_name = models.CharField(max_length=150, null=True, blank=True, verbose_name="etternavn")
    nickname = models.CharField(max_length=150, unique=True, null=True, blank=False, verbose_name="kallenavn")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None, null=True, blank=True, verbose_name="kjønn")
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=13, default=None, null=True, blank=True, verbose_name="mobilnummer")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, blank=True, editable=False, verbose_name="opprettet")

    objects = auth_models.UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'bruker'
        verbose_name_plural = 'brukere'
        ordering = ['username']

    def __str__(self):
        return f"{self.get_full_name() or self.username or self.email or self.id}"

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return None

    def get_username(self):
        return self.username

    def get_short_name(self):
        return self.first_name

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'nickname': self.nickname,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'department': self.department,
            'is_staff': self.is_staff,
            'is_superuser': self.is_superuser,
        }
