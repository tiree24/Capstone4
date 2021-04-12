from django.http import HttpResponseServerError
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import View
from .forms import FileUploadForm
from .models import FileUpload
from auth_app.models import MyCustomUser
from django.core.files.storage import FileSystemStorage


def my_test_500_view(request):
        # Return an "Internal Server Error" 500 response code.
        return HttpResponseServerError()

class UploadView(View):
    def get(self, request, user_id):
        user = MyCustomUser.objects.get(id=user_id)
        uploads = user.objects.all(files)
        form = FileUploadForm()
        return render(request, "upload.html", {
            "form" : form,
            "user" : user,
            'uploads' : uploads,
            })

    def post(self, request):
        context = {}
        if request.method =='POST':
            file_uploaded = request.FILES['upload']
            print(file_uploaded.name)
            fs = FileSystemStorage()
            name = fs.save(file_uploaded.name, file_uploaded)
            context['url'] = fs.url(name)
            context['form'] = FileUploadForm()
            return render(request, "upload.html", context)

        return HttpResponseRedirect(reverse('Upload', args=[user_id]))

def favorite(self, request, upload_id):
    upload = FileUpload.objects.get(id=upload_id)
    upload.favorite = True
    upload.save()
    return HttpResponseRedirect(reverse('Upload'))

def favorites(request):
    fav_files = MyCustomUser.objects.all(favorites)
    # request.user.favorites.add(fav_files)
    return render(request, 'favorites.html', {
        'favorites': fav_files
    })
    # return HttpResponseRedirect(reverse('recipe_detail', args=[favorite_id]))


    
