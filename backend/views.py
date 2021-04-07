# from django.shortcuts import render
# from django.http import HttpResponseServerError
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import View
from .forms import FileUploadForm
from .models import FileUpload
from django.core.files.storage import FileSystemStorage

# Create your views here.
# def my_test_500_view(request):
#         # Return an "Internal Server Error" 500 response code.
#         return HttpResponseServerError()

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