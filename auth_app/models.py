from django.db import models
from django.contrib.auth.models import AbstractUser

class MyCustomUser(AbstractUser):
    email = models.EmailField()
    password = models.CharField(max_length=20)
    favorite = models.ManyToManyField("FileUpload", related_name='user_favorites', blank=True)

    def __str__(self):
        return self.username