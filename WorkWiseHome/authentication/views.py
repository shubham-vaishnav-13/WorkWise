from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as auth_logout
from .models import UserProfile
# Create your views here.
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password'] 
        
        if not email or not password:
            messages.error(request, 'Email and password are required')
            return render(request, 'authentication/signin.html')
            
        try:
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged in!')
                # Get the user's profile ID
                user_profile = UserProfile.objects.get(user=user)
                return redirect(f'/{user_profile.id}/home')
            else:
                messages.error(request, 'Invalid credentials')
                return render(request, 'authentication/signin.html')
        except Exception as e:
            messages.error(request, 'An error occurred during login')
            return render(request, 'authentication/signin.html')
            
    return render(request, 'authentication/signin.html')

def signup(request):
    if request.method == 'POST':
        required_fields = ['full_name', 'email', 'phone', 'address', 'password', 'city', 'state']
       
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        if not phone.isdigit() or len(phone) != 10:
            messages.error(request, 'Please enter a valid 10-digit phone number')
            return render(request, 'authentication/signup.html')
        address = request.POST['address']
        password = request.POST['password']
        if (len(password) < 8 or 
            not any(char.isdigit() for char in password) or
            not any(char.isupper() for char in password) or 
            not any(char.islower() for char in password) or
            not any(char in '!@#$%^&*()' for char in password)):
            messages.error(request, 'Password must be at least 8 characters and contain uppercase, lowercase, number and special character')
            return render(request, 'authentication/signup.html')
        

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
                state=state,
                password=password
            )
            
            messages.success(request, 'Account created successfully')
            return redirect('signin')
        except Exception as e:
            messages.error(request, 'An error occurred during registration')
            
    return render(request, 'authentication/signup.html')

def logout(request):
    auth_logout(request)
    return redirect('/authentication/signin')


