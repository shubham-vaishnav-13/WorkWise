from django.shortcuts import render,redirect

# Create your views here.

def signin(request):
    return render(request,'authentication/signin.html')

def signup(request):
    return render(request,'authentication/signup.html')

def logout(request):
    return redirect('signin')