from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, mobile_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            mobile_number=mobile_number,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, mobile_number, password=None):
        user = self.create_user(email, mobile_number, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(max_length=250, unique=True)
    mobile_number = models.CharField(max_length=128, unique=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['mobile_number']
