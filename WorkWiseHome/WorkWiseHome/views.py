from django.http import HttpResponse
from django.shortcuts import render


# Direct Https Response
def home(request):
    return HttpResponse("Hello WorkWise First Page Testing")

