from secrets import choice
import uuid

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, cpf, name, password=None, role=None):
        if not cpf:
            raise ValueError('Users must have an CPF')

        user = self.model(
            cpf=cpf,
            name=name,
            role=role
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, cpf, name, password=None, role=None):
        if not cpf:
            raise ValueError('Users must have an CPF')

        user = self.model(
            cpf=cpf,
            name=name,
            role=role
        )

        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpf = models.CharField(
        max_length=11,
        unique=True,
    )

    name = models.CharField(max_length=100, blank=False, null=False)
    role = models.CharField(max_length=10)

    objects = UserManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['name','role']

    def __str__(self):
        return self.cpf