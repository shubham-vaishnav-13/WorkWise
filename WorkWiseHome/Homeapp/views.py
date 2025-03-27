from django.shortcuts import render, redirect
from .models import Service, Orders, OrderUpdate
from django.http import JsonResponse
from math import ceil
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from . import keys
from decimal import Decimal
# MERCHANT_KEY = 'bKMfNxPPf_QdZppa'
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.conf import settings


def main(request):
    return render(request,'base.html')

client = razorpay.Client(auth=('KEY_ID', 'KEY_SECRET'))

@login_required
def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You need to login first')
        return render(request, 'login.html')
    
    if request.method == "POST":
        items_json = request.POST.get('itemJson', '')
        name = request.POST.get('name', '')
        address = request.POST.get('addressline1', '') + " " + request.POST.get('addressline2', '')
        City = request.POST.get('City', '')
        state = request.POST.get('state', '')
        pincode = request.POST.get('pincode', '')
        phoneno = request.POST.get('phoneno', '')
        email = request.user.email
        amount = request.POST.get('amt', '')
        try:
            # Convert amount to Decimal and then to integer (in paise)
            amount = int(Decimal(amount) * 100)
        except (ValueError):
            messages.error(request, "Invalid amount provided.")
            return redirect('/checkout/')

        Order = Orders(
            items_json=items_json,
            name=name,
            phoneno=phoneno,
            address=address,
            city=City,
            state=state,
            pincode=pincode,
            amount=amount / 100,
            email=email
        )
        Order.save()

        # Razorpay payment gateway
        order_data = {
            'amount': amount,  # Pass the amount as an integer in paise
            'currency': 'INR',
            'receipt': str(Order.order_id),
            'payment_capture': '1'
        }

        razorpay_order = client.order.create(data=order_data)
        Order.razorpay_order_id = razorpay_order['id']  # Save the Razorpay order ID
        Order.save()

        return render(request, 'payment.html', {
            'order_id': razorpay_order['id'],
            'razorpay_key_id': 'KEY_ID',  # Replace with your Razorpay key ID
            'price': amount / 100
        })
    
    # Handle GET request
    return render(request, 'checkout.html')  # Render a checkout page for GET requests

@csrf_exempt
def verify_payment(request):    
    if request.method == 'POST':
        payment_response = json.loads(request.body)
        param_dict = {
            'razorpay_order_id': payment_response['razorpay_order_id'],
            'razorpay_payment_id': payment_response['razorpay_payment_id'],
            'razorpay_signature': payment_response['razorpay_signature']
        }

        try:
            client.utility.verify_payment_signature(param_dict)

            try:
                order = Orders.objects.get(razorpay_order_id=param_dict['razorpay_order_id'])
                order.razorpay_payment_id = param_dict['razorpay_payment_id']
                order.payment_verified = True
                order.save()
                return JsonResponse({'status': 'success', 'message': 'Payment successful'})
            
            except Orders.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Order not found'}, status=404)

        except razorpay.errors.SignatureVerificationError:
            return JsonResponse({'status': 'error', 'message': 'Payment verification failed'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

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

import json
from json.decoder import JSONDecodeError

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You need to login first')
        return render(request, 'authentication/login')
    currentUser = request.user.email
    items = Orders.objects.filter(email=currentUser)
    for order in items:
        try:
            parsed_items = json.loads(order.items_json)
            if isinstance(parsed_items, dict):
                order.parsed_items = parsed_items
            elif isinstance(parsed_items, list):
                order.parsed_items = {item: 1 for item in parsed_items}
            else:
                order.parsed_items = {}
            
        except JSONDecodeError:
            order.parsed_items = {}  

        order.payment_verified_status = order.payment_verified
        order.razorpay_payment_id_status = order.razorpay_payment_id
    
    context = {'items': items}
    return render(request, 'profile.html', context)