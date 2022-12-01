from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Gallery_Model


from .forms import GalleryForm


def Upload(request):
    form = GalleryForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            if form.save():
                print("성공")
            else:
                print("실패")
            uploads = Gallery_Model.objects
            return redirect('http://localhost:8000')
    else:
        form = GalleryForm()
        return render(request, 'gallery/upload.html',{'form': form})


def index(request):
    uploads = Gallery_Model.objects
    try:
        return render(request, 'gallery/index.html', {'uploads': uploads})
    except:
        return render(request, 'gallery/index.html')


