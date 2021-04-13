from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.views.generic import View, ListView
from .forms import FileUploadForm
from .models import FileUpload
from django.core.files.storage import FileSystemStorage
from capstone.settings import MEDIA_ROOT
from capstone import settings
import os


def handler404(request, exception):
    return render(request, "404.html")


def handler500(request):
    return render(request, "500.html")

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


def file_list(request):
    files = FileUpload.objects.all()
    return render(request, 'file_list.html', {"files": files})


def favorite(self, request, upload_id):
    upload = FileUpload.objects.get(id=upload_id)
    upload.favorite = True
    upload.save()
    return HttpResponseRedirect(reverse('Upload'))


def favorites(request):
    fav_files = FileUpload.objects.filter(favorite=True)
    # request.user.favorites.add(fav_files)
    return render(request, 'favorites.html', {
        'favorites': fav_files
    })
    # return HttpResponseRedirect(reverse('recipe_detail', args=[favorite_id]))

class SearchView(ListView):
    model = FileUpload
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = FileUpload.objects.filter(upload__icontains=q)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(results=self.results, **kwargs)
