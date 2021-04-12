from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views.generic import View 
from .forms import FileUploadForm
from .models import FileUpload
from auth_app.models import MyCustomUser
from django.core.files.storage import FileSystemStorage
from capstone.settings import MEDIA_ROOT
from capstone import settings
import os


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

class UploadView(View):
   
    def get(self, request):
        form = FileUploadForm()
        return render(request, "upload.html", {
            "form" : form,
            "user" : user,
            'uploads' : uploads,
            })

    def post(self, request):
        context = {}
        if request.method =='POST':
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                new_upload = FileUpload.objects.create(title=request.POST['title'], 
                upload=request.FILES['upload'],
                search_str=request.POST['search_str'],
                )
                return redirect('file_list')


def file_list(request):
    files = FileUpload.objects.all()
    return render(request, 'file_list.html', {"files": files})

<<<<<<< HEAD
        return HttpResponseRedirect(reverse('Upload', args=[user_id]))
=======
>>>>>>> 3a43033149c9c4c12f7bab2c7ca895d0829ff883

def favorite(self, request, upload_id):
    upload = FileUpload.objects.get(id=upload_id)
    upload.favorite = True
    upload.save()
    return HttpResponseRedirect(reverse('Upload'))
<<<<<<< HEAD

def favorites(request):
    fav_files = MyCustomUser.objects.all(favorites)
    # request.user.favorites.add(fav_files)
    return render(request, 'favorites.html', {
        'favorites': fav_files
    })
    # return HttpResponseRedirect(reverse('recipe_detail', args=[favorite_id]))


    
=======
>>>>>>> 3a43033149c9c4c12f7bab2c7ca895d0829ff883
