from .models import FileUpload
from django import forms

class FileUploadForm(forms.ModelForm):
    upload = forms.FileField(required=True)
    class Meta:
        model = FileUpload
        fields = ('title', 'upload', 'date_time', 'search_str')