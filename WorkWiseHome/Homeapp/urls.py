from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('',views.main,name="main"),
    path('home/',views.home,name="home"),
    path('checkout/',views.checkout,name="checkout"),
    path('get_service_details/<int:service_id>/', views.get_service_details, name='get_service_details'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)