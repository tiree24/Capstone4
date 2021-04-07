from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from backend.forms import LoginForm, FileUploadForm, CustomUserForm
from backend.models import FileUpload
from django.core.files.storage import FileSystemStorage


class LoginFormView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "generic_form.html", { 'form': form, 'heading': 'Login below'})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('Login')))

        
        form = LoginForm()
        return render(request, 'generic_form.html', {
            'heading': 'Login below',
            'form': form})

class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('Home'))



class UploadView(View):
    def get(self, request):
        form = FileUploadForm()
        return render(request, "upload.html", {"form" : form })

    def post(self, request):
        context = {}
        if request.method =='POST':
            file_uploaded = request.FILES['upload']
            print(file_uploaded.name)
            fs = FileSystemStorage()
            name = fs.save(file_uploaded.name, file_uploaded)
            context['url'] = fs.url(name)
         
            
        return render(request, "upload.html", context)



  
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

def FavoritesView(request):
    # fav_files = FileUpload.objects.get(id=favorite_id)
    # request.user.author.favorites.add(fav_files)
    return render(request, 'favorites.html')
    # return HttpResponseRedirect(reverse('recipe_detail', args=[favorite_id]))