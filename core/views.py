from django.shortcuts import render
from .forms import UploadImage
from .models import ImageUpload
# Create your views here.

def home(request):
    if request.method =='POST':
        form = UploadImage(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadImage()
    img = ImageUpload.objects.all()
    context = {'form':form,'img':img}
    return render(request,'core/home.html',context)