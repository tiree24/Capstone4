from django.db import models
from django.utils.timezone import now

class FileUpload(models.Model):  
    upload = models.FileField()
    date_time = models.DateTimeField(default=now)
    search_str = models.TextField(max_length=50)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.search_str
