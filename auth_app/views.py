from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from backend.forms import LoginForm

# Create your views here.

class LoginFormView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", { 'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, email=data['email'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('Login')))
        
        form = LoginForm()
        return render(request, 'login.html', {
            'heading': 'Login below',
            'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('Home'))