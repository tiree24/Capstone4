from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from backend.forms import FileUploadForm
from django.core.files.storage import FileSystemStorage
from .forms import LoginForm, CustomUserForm
from .models import MyCustomUser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginFormView(View):

    def get(self, request):
        form = LoginForm()
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('file_list'))
        else:
            return render(request, "login.html", { 'form': form, 'heading': 'Droppi'})

    def post(self, request):
        print('posted!!')
        form = LoginForm(request.POST)
        print('form', form)
        if form.is_valid():
            print('clean data', form.cleaned_data)
            data = form.cleaned_data
            print('data', data)
            user = authenticate(
                request, email=data['email'], password=data['password'])
            print('user', user)
            if user:
                login(request, user)
                return redirect('file_list')
            else:
                return HttpResponseRedirect(reverse('login'))

        else:
            return HttpResponseRedirect(reverse('login'))

@method_decorator(login_required, name='dispatch')
class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


def signup(request):

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyCustomUser.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            login(request, new_user)
            return redirect('file_list')
        else:
            return HttpResponseRedirect(reverse('signup'))

    form = CustomUserForm()
    return render(request, 'signup.html', {'form': form, 'heading': "Droppi"})

