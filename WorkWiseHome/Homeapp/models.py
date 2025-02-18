from django.db import models
from authentication.models import UserProfile
from django.contrib.auth.models import User
# Create your models here.



# class ServiceProvider(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='service_provider')
#     service_category = models.ForeignKey('ServiceCategory', on_delete=models.SET_NULL, null=True)
#     experience = models.IntegerField(default=0) 
#     available = models.BooleanField(default=True)
#     rating = models.FloatField(default=0.0)

#     def __str__(self):
#         return f"{self.user.username} - {self.service_category.name }"
    

# class ServiceCategory(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name

    

# class Service(models.Model):
#     provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
#     category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)  
#     duration = models.DurationField()  
#     def __str__(self):
#         return f"{self.title} - {self.provider.user.username}"


# class Booking(models.Model):
#     customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
#     date = models.DateField()
#     time = models.TimeField()
#     status = models.CharField(
#         max_length=20,
#         choices=[
#             ("Pending", "Pending"), 
#             ("Confirmed", "Confirmed"), 
#             ("Completed", "Completed"), 
#             ("Cancelled", "Cancelled")
#         ],
#         default="Pending",
#     )
#     transaction_id = models.CharField(max_length=255, blank=True, null=True) 

#     def __str__(self):
#         return f"{self.customer.full_name} - {self.service.title} - {self.status}"



# class Payment(models.Model):
#     booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=20, choices=[("Success", "Success"), ("Failed", "Failed"), ("Pending", "Pending")])
#     payment_date = models.DateTimeField(auto_now_add=True)
#     transaction_id = models.CharField(max_length=255, unique=True)

#     def __str__(self):
#         return f"Payment {self.transaction_id} - {self.status}"


# class Review(models.Model):
#     customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
#     rating = models.IntegerField(default=1)
#     comment = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.customer.full_name} - {self.provider.user.username} - {self.rating}"
