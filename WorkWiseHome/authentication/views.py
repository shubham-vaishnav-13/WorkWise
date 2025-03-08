from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as auth_logout
from .models import UserProfile
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.views import View
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
                # messages.success(request, 'Login successful')
                return redirect('/')
            else:
                messages.error(request, 'Invalid credentials')
                return render(request, 'authentication/signin.html')
        except Exception as e:
            messages.error(request, 'An error occurred during login')
            return render(request, 'authentication/signin.html')
            
    return render(request, 'authentication/signin.html')

def signup(request):
    if request.method == 'POST':
       
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

            # Create user and profile
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
            user.is_active = False
            email_subject = 'Activate your account'
            message = render_to_string('authentication/activate.html', {
                'user': user,
                'domain': '127.0.0.1:8000', # Added missing comma here
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
                })
            email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
            email_message.send()
            messages.success(request, 'Registration successful. Please check your email to activate your account')
            user.save()
            request.session['registration_success'] = True
            return render(request,'authentication/signup.html')

        except Exception as e:
            print(f"Registration error: {str(e)}")
            messages.error(request, 'An error occurred during registration')
            return render(request, 'authentication/signup.html')
            
    return render(request, 'authentication/signup.html')


class ActiviateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as e:
            user = None
        if user is not None and generate_token.check_token(user,token):
            user.is_active = True
            user.save()
            messages.success(request, 'Account activated successfully')
            return redirect('/authentication/signin')
        return redirect('/authentication/signup')
    


def logout(request):
    auth_logout(request)
    messages.success(request, 'Logout successful')
    return redirect('/authentication/signin')


