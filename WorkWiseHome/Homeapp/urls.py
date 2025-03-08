from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('',views.main,name="main"),
    path('home/',views.home,name="home"),
    path('cleaning/',views.cleaning,name="cleaning"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)