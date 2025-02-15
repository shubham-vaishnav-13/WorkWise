from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as auth_logout
from .models import UserProfile
# Create your views here.

def signin(request):
    if request.method == 'POST':
        if 'email' not in request.POST or 'password' not in request.POST:
            messages.error(request, 'Please provide both email and password')
            return render(request, 'authentication/signin.html')
            
        email = request.POST['email']
        password = request.POST['password']
        
        if not email or not password:
            messages.error(request, 'Email and password are required')
            return render(request, 'authentication/signin.html')
            
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'authentication/signin.html')

def signup(request):
    if request.method == 'POST':
        required_fields = ['full_name', 'email', 'phone', 'address', 'password', 'city', 'state']
        for field in required_fields:
            if field not in request.POST:
                messages.error(request, f'{field.replace("_", " ").title()} is required')
                return render(request, 'authentication/signup.html')
        
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        city = request.POST['city']
        state = request.POST['state']

        if not all([full_name, email, phone, password]):
            messages.error(request, 'Please fill in all required fields')
            return render(request, 'authentication/signup.html')

        
        try:
            if User.objects.filter(username=email).exists():
                messages.error(request, 'Email already exists')
                return render(request, 'authentication/signup.html')
        except Exception as identifier:
            messages.error(request, 'An error occurred during registration')
            return render(request, 'authentication/signup.html')

        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            UserProfile.objects.create(
                user=user,
                full_name=full_name,
                phone=phone,
                address=address,
                city=city,
                state=state
            )
            messages.success(request, 'Account created successfully')
            return redirect('signin')
        except Exception as e:
            messages.error(request, 'An error occurred during registration')
            
    return render(request, 'authentication/signup.html')

def logout(request):
    auth_logout(request)
    return redirect('signin')


