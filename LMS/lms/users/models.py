from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username
