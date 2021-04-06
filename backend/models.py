from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.conf import settings



class CustomUserModel(AbstractUser):
    profile_name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
            return self.profile_name



