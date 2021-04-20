from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class MyCustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    password = models.CharField(max_length=20)
    favorites = models.ManyToManyField('backend.FileUpload', related_name='user_favorites', blank=True)

    def __str__(self):
        return self.email