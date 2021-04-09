from django.http import HttpResponseServerError
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views.generic import View 
from .forms import FileUploadForm
from .models import FileUpload
from django.core.files.storage import FileSystemStorage
from capstone.settings import MEDIA_ROOT
from capstone import settings
import os



def my_test_500_view(request):
        # Return an "Internal Server Error" 500 response code.
        return HttpResponseServerError()

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
            context['form'] = FileUploadForm()
            return render(request, "upload.html", context)

        return HttpResponseRedirect(reverse('Upload'))

class File_list(View):
    def list(self, request):
        files = FileUpload.objects.all()
        return render(request, 'file_list.html', {"files": files})
    # media_url = settings.MEDIA_URL
    # path_to_user_folder = media_url + "/upload/"
    # context = {
    #     'files': FileUpload.objects.all(),
    #     'media_url': settings.MEDIA_URL,
    # }      
    # myfiles = [f for f in listdir(media_path) if isfile(join(media_path, f))]
    
    # media_path = settings.MEDIA_ROOT
    # files = os.listdir(media_path)
    # print(files)
    # string = ''.join(f for f in files)
    # my_files = FileUpload()
   

def upload_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            title = FileUpload.objects.create(title=form.cleaned_data['title'],
                date_time=form.data['date_time'],
                search_str=form.data['search_str'])
            new_file = FileUpload(file = request.FILES['file'])
            form.save()
            return redirect('files_list')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {"form": form})
