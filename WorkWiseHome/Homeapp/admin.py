from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.ServiceProvider)
admin.site.register(models.Service)
admin.site.register(models.Orders)
admin.site.register(models.OrderUpdate)

# Ctrl + I 
