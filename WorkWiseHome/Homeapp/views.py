from django.shortcuts import render
from .models import Service, Orders, OrderUpdate
from django.http import JsonResponse
from math import ceil
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from . import keys
MERCHANT_KEY = keys.MK
# Create your views here.
from PayTm import Checksum

def main(request):
    return render(request,'base.html')

@login_required
def checkout(request):
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

    if not request.user.is_authenticated:
        messages.warning(request, 'You need to login first')
        return render(request, 'login.html')
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amt = request.POST.get('amt', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('addressline1', '') + " " + request.POST.get('addressline2', '')
        City = request.POST.get('City', '')
        state = request.POST.get('state', '')
        pincode = request.POST.get('pincode', '')
        phoneno = request.POST.get('phoneno', '')
        email = request.user.email
        Order = Orders(items_json=items_json, name=name, phoneno=phoneno, address=address, city=City, state=state, pincode=pincode, amount=amt)
        
        Order.save()
    
        update = OrderUpdate(order_id=Order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True

        # Payment Integration

        id = Order.order_id
        oid = str(id) + "WorkWise"
        param_dict = {
            'MID':keys.MID,
            'ORDER_ID':oid,
            'TXN_AMOUNT':str(amt),
            'CUST_ID':email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
        }





    return render(request, 'checkout.html', params) 

def get_service_details(request, service_id):
    try:
        service = Service.objects.get(pk=service_id)
        data = {
            'name': service.title,
            'price': service.price,
        }
        return JsonResponse(data)
    except Service.DoesNotExist:
        return JsonResponse({'error': 'Service not found'}, status=404)
    
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


