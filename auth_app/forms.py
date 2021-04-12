from .models import MyCustomUser
from django import forms

class CustomUserForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyCustomUser
        fields = ('email', 'username', 'password')

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyCustomUser
        fields = ('email', 'password')  


        
