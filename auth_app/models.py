from django.db import models
from django.contrib.auth.models import AbstractUser
from backend.models import FileUpload

class MyCustomUser(AbstractUser):
    email = models.EmailField()
    password = models.CharField(max_length=20)
    favorites = models.ManyToManyField(FileUpload, related_name='user_favorites', blank=True)

    def __str__(self):
        return self.username