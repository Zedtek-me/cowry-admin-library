from django.db import models
from django.contrib.auth.models import AbstractUser
from interfaces.models import BaseModel
from library_admin_apps.users.managers import UserManager


class User(BaseModel, AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.email}"

    @property
    def id(self):
        return self._id


