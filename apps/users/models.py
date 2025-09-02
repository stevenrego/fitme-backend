from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # You can add custom fields here later, e.g. phone, avatar, etc.
    # phone = models.CharField(max_length=20, blank=True)
    pass
