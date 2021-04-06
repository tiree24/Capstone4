from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from backend.models import CustomUserModel
from backend.forms import CustomUserForm, LoginForm
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect, HttpResponse
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, 
                username=data['username'],
                password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
    form = LoginForm()            
    return render(request, 'generic_form.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homepage')     
    form = CustomUserForm()
    return render(request, "generic_form.html", {'form':form})

# @login_required(login_url='login/')
def homepage(request):
    user_data = CustomUserModel()
    return render(request, "homepage.html", {'user_data':user_data, 'auth': settings.AUTH_USER_MODEL})
