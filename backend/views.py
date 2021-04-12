from django.http import HttpResponseServerError
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views.generic import View 
from .forms import FileUploadForm
from .models import FileUpload
from django.core.files.storage import FileSystemStorage
from capstone.settings import MEDIA_ROOT
from capstone import settings
import os
from django.shortcuts import get_object_or_404
from django.http import Http404





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
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                new_upload = FileUpload.objects.create(title=request.POST['title'], 
                upload=request.FILES['upload'],
                search_str=request.POST['search_str'],
                )
                return redirect('file_list')
    # def recent(self, request):
    #     file = FileUpload.objects.all().order_by('-date_time')
    #     obj= FileUpload.objects.filter(testfield=12).order_by('-id')[2]
    #     return redirect('file_list')

    


def file_list(request):
    files = FileUpload.objects.all().order_by('-date_time')
    recent = FileUpload.objects.all().order_by('-date_time')[:3]
    return render(request, 'file_list.html', {"files": files, "recent": recent})

def delete_file(request, pk):
    if request.method == "POST":
        files = FileUpload.objects.get(pk=pk)
        files.deleted()
        return redirect('/files/')
    return redirect('/files')

   


# deleting instance from db
# delete file form sys

