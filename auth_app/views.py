from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from backend.forms import FileUploadForm
from django.core.files.storage import FileSystemStorage
from .forms import LoginForm, CustomUserForm
from .models import MyCustomUser


class LoginFormView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "generic_form.html", { 'form': form, 'heading': 'Login below'})

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
                return HttpResponseRedirect(request.GET.get('next', reverse('Upload')))
            else:
                return HttpResponseRedirect(reverse('Login'))


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('Login'))


def signup_view(request):

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyCustomUser.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            
            # user = authenticate(email=email, password=password)
            login(request, new_user)
            return redirect('Upload')
        else:
            return HttpResponseRedirect(reverse('Signup'))

    form = CustomUserForm()
    return render(request, 'generic_form.html', {'form': form, 'heading': "Sign Up below"})

