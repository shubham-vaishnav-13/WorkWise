from django.urls import include, path

from . import views
urlpatterns = [
    path('',views.main,name="main"),
    path('home/',views.home,name="home"),
    path('cleaning/',views.cleaning,name="cleaning"),
    path('repair/',views.repair,name="repair"),
    path('kitchen/',views.kitchen,name="kitchen"),



]