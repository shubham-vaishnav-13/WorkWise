from django.shortcuts import render
from .models import Service
from math import ceil
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    return render(request,'base.html')

@login_required
def checkout(request):
    return render(request,'checkout.html')

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


