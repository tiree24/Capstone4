from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views.generic import View 
from .forms import FileUploadForm
from .models import FileUpload
from auth_app.models import MyCustomUser
from django.core.files.storage import FileSystemStorage
from capstone.settings import MEDIA_ROOT
from capstone import settings
import os
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# def my_test_500_view(request):
#         # Return an "Internal Server Error" 500 response code.
#         return HttpResponseServerError()

# class UploadView(View):
#     def get(self, request, user_id):
#         user = MyCustomUser.objects.get(id=user_id)
#         uploads = user.objects.all(files)
def handler404(request, exception):
    return render(request, "404.html")


def handler500(request):
    return render(request, "500.html")

@method_decorator(login_required, name='dispatch')
class UploadView(View):
   
    def get(self, request):
        form = FileUploadForm()
        return render(request, "upload.html", {
            "form" : form,
            })

    def post(self, request):
        context = {}
        if request.method =='POST':
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                new_upload = FileUpload.objects.create(
                title=request.POST['title'], 
                upload=request.FILES['upload'],
                search_str=request.POST['search_str'],
                )
                new_upload.created_by.set(MyCustomUser.objects.filter(id=request.user.id))
                new_upload.save()
                return redirect('file_list')

@login_required()
def file_list(request):
    files = FileUpload.objects.filter(created_by=request.user).order_by('-date_time')
    return render(request, 'file_list.html', {"files": files})

@login_required()
def favorite(request, upload_id):
    upload = FileUpload.objects.get(id=upload_id)
    user = MyCustomUser.objects.get(id=request.user.id)

# if upload_id not in user.favorites:
    user.favorites.add(upload)
    upload.save()
    return HttpResponseRedirect(reverse('Favorites'))

@login_required()
def unfavorite(request, upload_id):
    upload = FileUpload.objects.get(id=upload_id)
    user = MyCustomUser.objects.get(id= request.user.id)
    user.favorites.remove(upload)
    upload.save()
    return HttpResponseRedirect(reverse('Favorites'))

@login_required()
def favorites(request):
    fav_files = request.user.favorites.all()
    return render(request, 'favorites.html', {
        'favorites': fav_files
    })


    
