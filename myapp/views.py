from django.shortcuts import render
from .form import ImageForm
from .models import Image
# Create your views here.

def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    img = Image.objects.all()
    form = ImageForm
    return  render(request,"index.html",{'form':form,'img':img})