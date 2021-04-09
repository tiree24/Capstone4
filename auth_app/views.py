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
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('Upload')
        else:
            return HttpResponseRedirect(reverse('Login'))

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
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('Upload')
        else:
            return HttpResponseRedirect(reverse('Signup'))


def FavoritesView(request):
    # fav_files = FileUpload.objects.get(id=favorite_id)
    # request.user.author.favorites.add(fav_files)
    return render(request, 'favorites.html')
    # return HttpResponseRedirect(reverse('recipe_detail', args=[favorite_id]))
