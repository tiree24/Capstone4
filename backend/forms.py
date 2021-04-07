from backend.models import MyCustomUser, FileUpload
from django import forms

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyCustomUser
        fields = ('email', 'username', 'password')

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyCustomUser
        fields = ('email', 'password')


class FileUploadForm(forms.ModelForm):
    upload = forms.CharField(widget=forms.FileInput)
    class Meta:
        model = FileUpload
        fields = ('upload', 'date_time', 'search_str')