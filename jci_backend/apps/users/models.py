from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(blank=True)
    surname = models.CharField(blank=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()
