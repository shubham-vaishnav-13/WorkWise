from django.shortcuts import render
from .models import Service
from math import ceil

# Create your views here.

def main(request):
    return render(request,'base.html')

def home(request, id=None):
    allServices = []
    servProd = Service.objects.values('category', 'service_id')
    cats = {item['category'] for item in servProd}
    
    # Process each category separately
    for cat in cats:
        serv = Service.objects.filter(category=cat)
        n = len(serv)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allServices.append([serv, range(1, nSlides), nSlides])
    allServices.sort(key=lambda x: x[0][0].category if x[0] else "")

    params = {'allServices': allServices}
    # Pass params instead of allServices
    return render(request, 'home.html', params)

def cleaning(request,id=None):
    allServices = []
    servProd = Service.objects.values('category', 'service_id')
    cats = {item['category'] for item in servProd}
    
    # Process each category separately
    for cat in cats:
        serv = Service.objects.filter(category=cat)
        n = len(serv)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allServices.append([serv, range(1, nSlides), nSlides])
    # If you want to sort the categories
    allServices.sort(key=lambda x: x[0][0].category if x[0] else "")
    params = {'allServices': allServices}
    return render(request,'cleaning.html',params)

