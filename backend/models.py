from django.db import models
# from auth_app.models import MyCustomUser
from django.utils.timezone import now

class FileUpload(models.Model):  
    upload = models.FileField()
    date_time = models.DateTimeField(default=now)
    search_str = models.TextField(max_length=50)
    favorite = models.BooleanField(default=False)
    # uploaded_by = models.ManyToManyField(MyCustomUser, null=True, on_delete=models.CASCADE, related_name="uploaded_by")

    def __str__(self):
        return self.search_str
