from django.contrib.auth.models import AbstractUser from django.db import models

class User(AbstractUser): class Roles(models.TextChoices): USER = 'user', 'User' COACH = 'coach', 'Coach' ADMIN = 'admin', 'Admin'

role = models.CharField(max_length=10, choices=Roles.choices, default=Roles.USER) email = models.EmailField(unique=True)

def save(self, *args, **kwargs):
    if not self.username:
        self.username = self.email
    return super().save(*args, **kwargs)_
