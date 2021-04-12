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
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                new_upload = FileUpload.objects.create(title=request.POST['title'], 
                upload=request.FILES['upload'],
                search_str=request.POST['search_str'],
                )
                return redirect('file_list')
    def recent(self, request):
        file = FileUpload.objects.all().order_by('-date_time')
        return redirect('file_list')

    def delete(self, request):
        if os.path.isfile(self.upload.path):
            os.remove(self.upload.path)






def file_list(request):
    files = FileUpload.objects.all()
    return render(request, 'file_list.html', {"files": files})
