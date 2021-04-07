from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyCustomUser, FileUpload

admin.site.register(MyCustomUser, UserAdmin)
admin.site.register(FileUpload)
