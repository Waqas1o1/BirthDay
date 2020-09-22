from django.shortcuts import render
from .models import Amna_Zafer
# Create your views here.
def index(request):
    return render(request,'birthday/index.html')
def Detail(request,pk):
    model = Amna_Zafer.objects.filter(id=pk)
    print(model)
    return render(request,'birthday/Detail.html',{'model':model})

def home(request):
    model = Amna_Zafer.objects.all()
    # print(model)
    return render(request,'birthday/home.html',{'Data':model})