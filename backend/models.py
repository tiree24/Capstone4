from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

class MyCustomUser(AbstractUser):
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FileUpload(models.Model):
    upload = models.FileField()
    date_time = models.DateTimeField(default=now)
    search_str = models.TextField(max_length=50)

    def __str__(self):
        return self.search_str