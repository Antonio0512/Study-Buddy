from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, max_length=100, null=False, blank=False)
    bio = models.TextField(null=True, blank=True)

    avatar = models.ImageField(null=True, blank=True, default="avatar.svg")
