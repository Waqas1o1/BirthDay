from django.shortcuts import render
from .models import EmanAlbum
# Create your views here.
def index(request):
    return render(request,'birthday/index.html')
def Detail(request,pk):
    model = EmanAlbum.objects.filter(id=pk)

    return render(request,'birthday/Detail.html',{'model':model})

def home(request):
    model = EmanAlbum.objects.all()
    # print(model)
    return render(request,'birthday/home.html',{'Data':model})