from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # Usuario personalizado: añade avatar, bio y reputación.
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    reputation = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    phone = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.username