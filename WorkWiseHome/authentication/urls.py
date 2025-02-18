from django.contrib import admin
from django.urls import include, path

from . import views
urlpatterns = [
    path('',views.signin,name="signin"),
    path('signin/',views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout,name="logout"),
    path('homeapp/',include('Homeapp.urls')),

]