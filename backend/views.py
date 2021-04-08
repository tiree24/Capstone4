from django.http import HttpResponseServerError
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views.generic import View
from .forms import FileUploadForm
from .models import FileUpload
from django.core.files.storage import FileSystemStorage


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

def file_list(request):
    files = FileUpload.objects.all()
    return render(request, 'file_list.html', {"files": files})

def upload_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files_list')
    
    else:
        form = FileUploadForm()
    return render(request, 'upload_file.html', {"form": form})
