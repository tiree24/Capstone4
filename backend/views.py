from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import View
from .forms import FileUploadForm
from .models import FileUpload
from django.core.files.storage import FileSystemStorage


def handler404(request, exception):
    return render(request, "404.html")


def handler500(request):
    return render(request, "500.html")


class UploadView(View):
    def get(self, request):
        form = FileUploadForm()
        return render(request, "upload.html", {"form": form})

    def post(self, request):
        context = {}
        if request.method == 'POST':
            file_uploaded = request.FILES['upload']
            print(file_uploaded.name)
            fs = FileSystemStorage()
            name = fs.save(file_uploaded.name, file_uploaded)
            context['url'] = fs.url(name)
            context['form'] = FileUploadForm()
            return render(request, "upload.html", context)

        return HttpResponseRedirect(reverse('Upload'))

def favorite(self, request, upload_id):
    upload = FileUpload.objects.get(id=upload_id)
    upload.favorite = True
    upload.save()
    return HttpResponseRedirect(reverse('Upload'))
