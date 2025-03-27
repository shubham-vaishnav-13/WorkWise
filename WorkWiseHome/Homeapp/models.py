from django.db import models

class ServiceProvider(models.Model):
    SERVICES = [
        ("Plumber", "Plumber"),
        ("Electrician", "Electrician"),
        ("Carpenter", "Carpenter"),
        ("Repair Technician", "Repair Technician"),
        ("Cleaner", "Cleaner"),
        ("Cook", "Cook"),
    ]
    service_provider_id = models.AutoField(primary_key=True)  # Fixed typo in field name
    service_provider_name = models.CharField(max_length=50, db_index=True)
    service_category = models.CharField(max_length=50, choices=SERVICES, db_index=True)
    experience = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.service_provider_name} - {self.service_category}"


class Service(models.Model):
    SERVICES = [
        ("Plumber", "Plumber"),
        ("Electrician", "Electrician"),
        ("Carpenter", "Carpenter"),
        ("Repair Technician", "Repair Technician"),
        ("Cleaner", "Cleaner"),
        ("Cook", "Cook"),
    ]

    service_id = models.AutoField(primary_key=True)
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, related_name="services")
    category = models.CharField(max_length=50, choices=SERVICES, db_index=True)  # Ensure same choices for consistency
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    duration = models.PositiveIntegerField(default=30)  # Assuming duration in minutes
    service_image = models.ImageField(upload_to="service_images/", blank=True, null=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.title} - {self.provider.service_provider_name}"


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    email = models.EmailField(default="")
    items_json = models.TextField()
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=15)
    razorpay_order_id = models.CharField(max_length=50, default="")
    razorpay_payment_id = models.CharField(max_length=50, default="")
    payment_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Order ID: {self.order_id} - {self.name}"
    

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.TextField()
    deliverd = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:8] + "..."    