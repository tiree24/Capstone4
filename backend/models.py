from django.db import models
from django.contrib.auth import admin

class CustomUser(AbstractUser):
    email = models.EmailField()
    password = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

