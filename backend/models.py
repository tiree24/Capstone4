from django.db import models
from django.utils.timezone import now

class FileUpload(models.Model):
    title = models.CharField(max_length=100)
    upload = models.FileField(upload_to='settings.MEDIA_URL')
    date_time = models.DateTimeField(default=now)
    search_str = models.TextField(max_length=50)
   
    

    def __str__(self):
        return self.search_str
    def __str__(self):
        return self.title
    def __str__(self):
        return self.upload.name
