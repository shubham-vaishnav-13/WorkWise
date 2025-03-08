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
