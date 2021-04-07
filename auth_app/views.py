from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import LoginForm, CustomUserForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class LoginFormView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "generic_form.html", { 'form': form, 'heading': 'Login below'})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, email=data['email'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('Upload')))


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('Login'))


class SignupFormView(View):

    def get(self, request):
        form = CustomUserForm()
        return render(request, 'generic_form.html', {'form': form, 'heading': "Sign Up below"})

    def post(self, request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(new_user.password)
            new_user.save()
            return HttpResponseRedirect(request.GET.get('next', reverse('Login')))
