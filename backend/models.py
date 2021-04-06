from django.db import models
from django.contrib.auth import admin
from django.utils.timezone import now

class CustomUser(AbstractUser):
    email = models.EmailField()
    password = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class FileUpload(models.Model):
    upload = models.FileField()
    date_time = models.DateTimeField()
    search_str = models.TextField(max_length=50)

    def __str__(self):
        return self.date_time