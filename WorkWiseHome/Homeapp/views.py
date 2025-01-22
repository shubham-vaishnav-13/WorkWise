from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')
def cleaning(request):
    return render(request,'cleaning.html')
def repair(request):
    return render(request,'repair.html')
def kitchen(request):
    return render(request,'kitchen.html')