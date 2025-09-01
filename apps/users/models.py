# apps/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Add custom fields later if needed, e.g.:
    # phone = models.CharField(max_length=20, blank=True)
    pass

                                                      ^^^^
