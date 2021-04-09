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
        files = []
        if request.method =='POST':
            file_uploaded = request.FILES['upload']
            print(file_uploaded.name)
            fs = FileSystemStorage()
            name = fs.save(file_uploaded.name, file_uploaded)
            context['urls']= files.append(fs.url(name))
            context['url'] = fs.url(name)
            context['form'] = FileUploadForm()
            return render(request, "upload.html", context)

        return HttpResponseRedirect(reverse('Upload'))

def file_list(request, **kwargs):
    # media_url = settings.MEDIA_URL
    # path_to_user_folder = media_url + "/upload/"
    # context = {
    #     'files': FileUpload.objects.all(),
    #     'media_url': settings.MEDIA_URL,
    # }      
    # media_path = settings.MEDIA_ROOT
    # myfiles = [f for f in listdir(media_path) if isfile(join(media_path, f))]
    # files = os.listdir(media_path)
    # print(files)
    # for file in files:
    #     if file:
    #         file.join(media_path)
    #     print(file)
    media_path = settings.MEDIA_ROOT
    files = os.listdir(media_path)
    # string = ''.join(f for f in files)
    # print(string)
    # my_files = [f.files for f in FileUpload.objects.all().order_by('-date_time')]

    
    return render(request, 'file_list.html', {"files": files})

# def upload_file(request):
#     if request.method == "POST":
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             title = FileUpload.objects.create(title=form.cleaned_data['title'])
#             new_file = FileUpload(file = request.FILES['file'])
#             form.save()
#             return redirect('files_list')
#     else:
#         form = FileUploadForm()
#     return render(request, 'upload.html', {"form": form})
