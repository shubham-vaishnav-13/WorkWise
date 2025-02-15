from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'base.html')

def home(request,id=None):
    return render(request,'home.html',{'id':id})
def cleaning(request,id=None):
    return render(request,'cleaning.html',{'id':id})
def repair(request,id=None):
    return render(request,'repair.html',{'id':id})
def kitchen(request,id=None):
    return render(request,'kitchen.html',{'id':id})